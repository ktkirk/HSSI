package main

import (
  "fmt"

  "github.com/hybridgroup/gobot"
  "github.com/hybridgroup/gobot/platforms/intel-iot/edison"
  "github.com/hybridgroup/gobot/platforms/gpio"
  "github.com/hybridgroup/gobot/platforms/i2c"
)

func main() {
  gbot := gobot.NewGobot()

  edisonAdaptor := edison.NewEdisonAdaptor("edison")
  blinkm := i2c.NewBlinkMDriver(edisonAdaptor, "blinkm")
  sensor := gpio.NewAnalogSensorDriver(edisonAdaptor, "sensor", "2")

  work := func() {
    gobot.On(sensor.Event("data"), func(data interface{}) {
      brightness := uint8(
        gobot.ToScale(gobot.FromScale(float64(data.(int)), 0, 4096), 0, 255),
      )
      fmt.Println("sensor", data)
      fmt.Println("brightness", brightness)
      blinkm.Rgb(0, brightness, 0)
    })
  }

  robot := gobot.NewRobot("sensorBot",
    []gobot.Connection{edisonAdaptor},
    []gobot.Device{blinkm, sensor},
    work,
  )

  gbot.AddRobot(robot)

  gbot.Start()
}
