var speed = [];
  speed[0] = {{ lastMeasuredWindSpeed|tojson|safe }};
  var windGConfig = {
    "type":"gauge",
    "background-color":"transparent",
    "bgcolor": "transparent",
    "scale":{
      "size-factor":1
    },
    "scale-r":{ //Default Scale
      "aperture":200,
      "values":"0:5:1",
      "center":{
        "size": 5,
        "background-color":"#66CCFF #FFCCFF",
        "border-color":"none"
      }

    },
    "series":[
      {
        "values":speed,
        "valueBox":{
            "text": "%v m/s",
            "placement": "center",
            "offsetY": 45,
            "fontSize": 12,
            "fontColor": "#515151",
          }
      }
    ]
  };