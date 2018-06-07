package controllers

import (
	"bytes"
	"encoding/json"
	"errors"
	"fmt"
	"io/ioutil"
	"net/http"
	"strconv"
	"strings"
	"demo/github.com/astaxie/beego"
)
var matrixServer = "http://39.104.109.10:7601/rec/image/batch"
var matrixServerSingle = "http://39.104.109.10:7601/rec/image"
var rankerServer = "http://39.104.109.10:6701/rank"
type MainController struct {
	beego.Controller
}
type AnController struct {
        beego.Controller
}
type PingController struct {
        beego.Controller
}


type Request struct {
	FaceID1   string `json:"face_id_1"`
	FaceID2   string `json:"face_id_2"`
	ImageURL1 string `json:"image_url_1"`
	ImageURL2 string `json:"image_url_2"`
	Face string `json:"face"`
}

type Response struct {
	Rtn        int     `json:"rtn"`
	Message    string  `json:"message"`
	FaceID1    string  `json:"face_id_1"`
	FaceID2    string  `json:"face_id_2"`
	Similarity float32 `json:"similarity"`
}
type AnResponse struct {
        Rtn        int     `json:"rtn"`
        Message    string  `json:"message"`
        Sex    string  `json:"sex"`
        Age    int  `json:"age"`
}
type PingResponse struct {
	Message	string `json:"message"`
}

type PostData struct {
	Context struct {
		SessionId string
		Type      int
		Functions []int
	}
	Images [2]struct {
		Data struct {
			URI string `json:"URI"`
		}
	}
	Image struct {
                Data struct {
                        URI string `json:"URI"`
                }
        }
	ObjectFeature struct {
		Feature string `json:"Feature"`
	}
	Params struct {
		Normalization string `json:"Normalization"`
	}
	ObjectCandidates [1]struct {
		Feature string `json:"Feature"`
	}
}

type Result struct {
	Context struct {
		Status     string
		StatusCode int
		Message    string
	}
	Results [2]struct {
		Faces [1]struct {
			Features string
		}
	}
	Result struct {
                Faces [1]struct {
			Attributes [2]struct {
			ValueInt int
			ValueString string
			}
                }
        }
	Candidates [1]struct {
		Score float32
	}
}
func (this *PingController) Get() {
        response := &PingResponse{
                Message:    "OK",
        }
        this.Data["json"] = response
        this.ServeJSON()
        return
}

func postData(uri string, data PostData) (*Result, error, int) {
	var err error

	requestJson, err := json.Marshal(data)
	if err != nil {
		return nil, err, 500
	}

	response, err := http.Post(uri, "application/json", bytes.NewBuffer([]byte(requestJson)))
	if err != nil {
		return nil, err, 500
	}

	responseJson, err := ioutil.ReadAll(response.Body)
	if err != nil {
		return nil, err, 500
	}

	ret := &Result{}
	json.Unmarshal(responseJson, &ret)

	ret.Context.StatusCode, err = strconv.Atoi(ret.Context.Status)
	if err != nil {
		return nil, err, 500
	}

	if !strings.Contains(ret.Context.Message, "SUCCESS") && len(ret.Context.Message) > 0 {
		return nil, errors.New(ret.Context.Message), ret.Context.StatusCode
	}

	return ret, nil, 200
}

func (this *MainController) SendError(statusCode int, err error, faceID1, faceID2 string) {
	response := &Response{
		Rtn:     statusCode,
		Message: err.Error(),
		FaceID1: faceID1,
		FaceID2: faceID2,
	}
	this.Data["json"] = response
	this.ServeJSON()
}

func (this *MainController) Post() {
	request := &Request{}
	json.Unmarshal(this.Ctx.Input.RequestBody, request)

	var matrixPostData PostData
	matrixPostData.Context.SessionId = "1vs1"
	matrixPostData.Context.Type = 2
	matrixPostData.Context.Functions = []int{200, 201, 202, 203, 204, 205}
	matrixPostData.Images[0].Data.URI = request.ImageURL1
	matrixPostData.Images[1].Data.URI = request.ImageURL2

	ret, err, status := postData(matrixServer, matrixPostData)
	if err != nil {
		this.SendError(status, err, request.FaceID1, request.FaceID2)
		return
	}
	if len(ret.Results) != 2 || len(ret.Results[0].Faces) != 1 || len(ret.Results[0].Faces[0].Features) == 0 {
		this.SendError(500, errors.New(fmt.Sprintf("Can not find face feature in %s", request.FaceID1)), request.FaceID1, request.FaceID2)
		return
	}
	if len(ret.Results) != 2 || len(ret.Results[1].Faces) != 1 || len(ret.Results[1].Faces[0].Features) == 0 {
		this.SendError(500, errors.New(fmt.Sprintf("Can not find face feature in %s", request.FaceID2)), request.FaceID1, request.FaceID2)
		return
	}

	var rankerPostData PostData
	rankerPostData.ObjectFeature.Feature = ret.Results[0].Faces[0].Features
	rankerPostData.Params.Normalization = "true"
	rankerPostData.ObjectCandidates[0].Feature = ret.Results[1].Faces[0].Features

	ret, err, status = postData(rankerServer, rankerPostData)
	if err != nil {
		this.SendError(status, err, request.FaceID1, request.FaceID2)
		return
	}
	if len(ret.Candidates) == 0 {
		this.SendError(500, errors.New("Can not find rank result"), request.FaceID1, request.FaceID2)
		return
	}

	response := &Response{
		Rtn:        200,
		Message:    "OK",
		FaceID1:    request.FaceID1,
		FaceID2:    request.FaceID2,
		Similarity: ret.Candidates[0].Score,
	}
	this.Data["json"] = response
	this.ServeJSON()
	return
}
func (this *AnController) SendError(statusCode int, err error) {
        response := &AnResponse{
                Rtn:     statusCode,
                Message: err.Error(),
                Sex: "null",
                Age: 0,
        }
        this.Data["json"] = response
        this.ServeJSON()
}

func (this *AnController) Post() {
	request := &Request{}
        json.Unmarshal(this.Ctx.Input.RequestBody, request)
	var matrixPostData PostData
        matrixPostData.Context.SessionId = "one person"
        matrixPostData.Context.Type = 2
        matrixPostData.Context.Functions = []int{200, 201, 202, 203, 204, 205}
        matrixPostData.Image.Data.URI = request.Face

        ret, err, status := postData(matrixServerSingle, matrixPostData)
	if err != nil {
		fmt.Println("err")
                this.SendError(status, err)
                return
        }
	fmt.Println(ret.Result.Faces[0].Attributes[0].ValueInt)
	fmt.Println(ret.Result.Faces[0].Attributes[1].ValueString)
	response := &AnResponse{
                Rtn:        200,
                Message:    "OK",
                Age:    ret.Result.Faces[0].Attributes[0].ValueInt,
		Sex:    ret.Result.Faces[0].Attributes[1].ValueString,
        }
        this.Data["json"] = response
        this.ServeJSON()
        return
}
