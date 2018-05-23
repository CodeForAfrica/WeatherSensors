temp = { timeseries|tojson|safe };
precipTimeList = (Object.keys(temp.precipitation)).sort();
values=[];
for (var i=0; i < timeList.length; i++) {
  values.push(temp.precipitation[precipTimeList[i]]);
}
var myConfig = {
  "type":"heatmap",
  "plot":{
    "aspect":"vertical"
  },
  "plotarea":{
    "adjust-layout":"auto"
  },
  "utc": true,
  "scaleY": {
    "visible": false
  },
   "scaleX":{
     "minValue": '{{ startTime }}',
     "step": 3600000,
      "transform":{
       "type": 'date',
       "all": '%D, %d %M<br>%h:%i %A',
       "itemsOverlap": true
     },
     "item": {
       "fontSize": 10
     },
     "maxItems": 13,
     "guide": {
       "visible": false
     }
   },
  "series":[
    {
      "values": values
    }
  ]
};

zingchart.render({
  id : 'precipitationChart',
  data : myConfig,
  height : "100px",
  width: "100%"
});