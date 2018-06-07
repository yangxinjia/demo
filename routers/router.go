package routers

import (
	"demo/controllers"
	"demo/github.com/astaxie/beego"
)

func init() {
    beego.Router("/demo/1vs1", &controllers.MainController{})
    beego.Router("/demo/an", &controllers.AnController{})
    beego.Router("/demo/ping",&controllers.PingController{})
}
