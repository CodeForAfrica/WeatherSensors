temp = {{ timeseries|tojson|safe }};
    pressureTimeList = (Object.keys(temp.atmosphericpressure)).sort();
    values=[];
    for (var i=0; i < timeList.length; i++) {
        values.push(temp.atmosphericpressure[pressureTimeList[i]]);
    }
    var pressureSecConfig = {
        "type": "area",
        "utc": true,
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
        "scale-y":{
            "values":"99:105:0.5",
            "format":"%v \u00B0C",
            "guide":{
            "visible":false
            }
        },
        "plot":{
        "tooltip": {
            "visible": true
            }
        },
        "series": [
        {
        "values": values,
        "lineColor": '#03A9F4',
        "backgroundColor":"#03A9F4",
        "lineWidth":0.5,
        "marker": {
            "backgroundColor": '#03A9F4',
            "borderWidth": 0,
            "size": 2
        }
        }
    ]
    };

    zingchart.render({
        id : 'pressureSection',
        data : pressureSecConfig,
        height: "200px",
        width: "100%"
});