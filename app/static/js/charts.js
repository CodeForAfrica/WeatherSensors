var myConfig17 = {
  "type":"gauge",
  "background-color":"transparent",
  "bgcolor": "transparent",
  "scale":{
    "size-factor":1
  },
  "scale-r":{
    "aperture":200,
    "values":"0:100:20",
    "center":{
      "size":5,
 	    "background-color":"#66CCFF #FFCCFF",
 	    "border-color":"none"
    },
    "ring":{
      "size":10,
      "rules":[
        {
          "rule":"%v >= 0 && %v <= 20",
 	        "background-color":"blue"
        },
        {
          "rule":"%v >= 20 && %v <= 40",
 	        "background-color":"green"
        },
        {
          "rule":"%v >= 40 && %v <= 60",
 	        "background-color":"yellow"
        },
        {
          "rule":"%v >= 60 && %v <= 80",
 	        "background-color":"orange"
        },
        {
          "rule":"%v >= 80 && %v <=100",
          "background-color":"red"
        }
      ]
    },
    "guide":{
      "alpha":0.5
    },
    "tick":{
      "line-color":"#66CCFF",
      "line-style":"solid",
      "line-width":3,
      "size":15,
      "placement":"inner"
    },
    "minor-ticks":4,
    "minor-tick":{
      "line-color":"#FFFFFF",
      "line-style":"solid",
      "line-width":2,
      "size":10,
      "placement":"inner"
    }
  },
  "plot":{
    "csize":"5%",
    "size":"100%",
    "background-color":"#000000",
    "animation":{ //Animation object
 	    "effect":2,
 	    "method":3,
 	    "sequence":1,
 	    "speed":3000
 	  }
  },
 	"tooltip":{
 	  "text":"%t - %v%",
 	  "font-color":"black",
 	  "font-family":"Georgia",
 	  "background-color":"white",
 	  "alpha":0.7,
 	  "border-color":"none"
 	},
  "series":[
    {
      "values":[87],
      "csize":"5%",
      "size":"90%",
      "text":"Very Great!"
    }
  ]
};

zingchart.render({
	id : 'windspeed',
	data : myConfig17,
	height : "350px",
	width: "100%"
});
