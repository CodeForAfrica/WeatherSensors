var temp = {{ lastMeasuredTemp|tojson|safe }};
var scaleFX = [];
var scaleFY = [];
scaleFY[0] = temp;
scaleFX[0] = temp + '\260' +"C";
var myTempConfig = {
  "type": "heatmap",
  "plot":{
    "tooltip":{
      "text":"It is %kl in Dar-es-salaam!",
      "background-color":"white",
      "alpha":0.9,
      "font-family":"Georgia",
      "font-color":"#000",
      "font-size":13
    },
    "aspect":"none",
    "background-color":"none",
    "background-repeat":false,
    "rules":[
      {
        "rule":"%v >= 28",
        "background-image":"//www.zingchart.com/package/examples/images/sunny.png"
      },
      {
        "rule":"%v >= 22 && %v <= 27",
        "background-image":"//www.zingchart.com/package/examples/images/partly-cloudy.png"
      },
      {
        "rule":"%v <= 21",
        "background-image":"//www.zingchart.com/package/examples/images/cloudy.png"
      }
    ],
    "hover-state":{
      "background-color":"#006699"
    }
  },
  "scale-x":{
    "labels":scaleFX,
    "line-color":"none",
    "guide":{
      "visible":false
    },
    "tick":{
      "visible":false
    },
    "item":{
      "font-color": "#515151",//"#024567",
      "font-size":12
    }
  },
  "scale-y":{
    "visible": false
  },
  "plotarea":{
    "margin-left":"dynamic",
  },
  "series": [
    {
      "values": scaleFY,
      "data-weather":["sunny"]
    },
  ]
  };

  zingchart.render({
  id : 'temperatureGauge',
  data : myTempConfig,
  height: "220px",
  width: "100%"
  });