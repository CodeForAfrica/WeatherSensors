zingchart.THEME="classic";
		var pressure = [];
		pressure[0] = {{ lastMeasuredPressure|tojson|safe }};
		var text = pressure[0] + " kPa"
		if (pressure[0] == "No record"){
			pressure[0] = "";
			text = "No record"
		}
		var pressureConfig = {
			type: "gauge",
			backgroundColor: "transparent",
			scaleR:{
				values: "0:30:5",
				aperture: 240,
				tick:{
					visible: false
				},
				item:{
					visible: false
				},
				ring:{
					backgroundColor: "transparent",
					// backgroundColor: "#C1C1C1",
					size: 10
				},
				center:{
					visible: false
				}
			},
			scale:{
				sizeFactor: 1.2
			},
			"scale-r-2":{
				values: "0:300:50",
				aperture: 220,
				tick:{
					lineWidth: 2,
					size: 6,
					lineColor: "#5F5F5F",
					placement: "outter"
				},
				minorTicks: 4,
				minorTick: {
					lineColor: "#C1C1C1",
					placement: "inner",
					size: 6
				},
				ring:{
					visible: false
				},
				item:{
					offsetR: -1,
					fontSize: 12
				},
				center:{
					size: 5,
					backgroundColor: "transparent",
				},
				label:{
					text: "text"
				}
			},
			"scale-2":{
				sizeFactor: 0.7
			},
			plot:{
				size: "56%",
				csize: "14%",
				tooltip:{
					visible: false
				}
			},
			plotarea:{
				marginBottom: "20%"
			},
			series : [
				{
					values : pressure,
					backgroundColor: "#F8B237",
					valueBox:{
						text: text,
						placement: "center",
						offsetY: 60,
						fontSize: 12,
						fontColor: "#515151",
					}

				}
			]
		};

	zingchart.render({
	id : 'pressureGauge',
	data : pressureConfig,
	height: "220px",
	width: "100%"
	});