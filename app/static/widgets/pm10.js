var precip = [];
                precip[0] = {{ lastMeasuredPrecip|tojson|safe }};
                var precipitationConfig = {
                    type:"bar",
                    x: "10%",
                    y: 0,
                    height: "100%",
                    width: "80%",
                    scaleY:{
                      lineColor: "none",
                      values: "0:100:10",
                      guide:{
                        visible: false
                      },
                      tick:{
                        margin: 1,
                        lineWidth: 1,
                        size: 10,
                        lineColor: "#5F5F5F",
                        placement: "outter",
                        rules:[
                          {
                            rule: "%i % 2 == 1",
                            lineWidth: 1
                          }
                        ]
                      },
                      minorTicks: 4,
                      minorTick: {
                        lineColor: "#C1C1C1",
                        placement: "inner",
                        size: 6
                      },
                      item:{
                        fontSize: 12,
                        rules:[
                          {
                            rule: "%i % 2 == 1",
                            visible: false
                          }
                        ]
                      }
                    },
                    "scale-y-2":{
                      values: "0:100:10",
                      lineColor: "none",
                      item:{
                        visible: false
                      },
                      guide:{
                        visible: false
                      },
                      tick:{
                        placement: "inner",
                        size: 40,
                        padding: 0,
                        margin: 0,
                        offsetX: 50,
                        lineColor: "#fff",
                        rules:[
                          {
                            rule: "%i == 0 || %i == 10",
                            visible: false
                          }
                        ]
                      }
                    },
                    plot:{
                      barsOverlap: "100%",
                      borderRadius: 2,
                      hoverState: {
                        visible: false
                      },
                      tooltip:{
                        visible: false
                      }
                    },
                    plotarea:{
                      marginBottom: "30%",
                      marginTop: "10%",
                      _marginRight: "35%"
                    },
                    scaleX:{
                      visible: false
                    },
                    series:[
                      {
                        values: [100],
                        backgroundColor: "#fff",
                        borderWidth: 4,
                        borderColor: "#C1C1C1",
                        maxTrackers: 0,
                        barWidth: "100%",
                        tooltip:{
                          visble: false
                        }
                      },
                      {
                        values: precip,
                        backgroundColor: "#F8B237",
                        barWidth: "93%",
                        maxTrackers: 0,
                        tooltip:{
                          visble: false
                        },
                        valueBox:{
                          text: "%v mm",
                          placement: "bottom-out",
                          offsetY: 0,
                          fontSize: 12,
                          fontColor: "#515151",
                        }
                      }
                    ]
                  };
                  zingchart.render({
                  id : 'precipitationGauge',
                  data : precipitationConfig,
                  height: "220px",
                  width: "100%"
                  });