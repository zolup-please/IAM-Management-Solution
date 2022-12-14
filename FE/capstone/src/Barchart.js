import * as React from 'react';
import { ResponsiveLine } from "@nivo/line";


const Barchart = (e) => {

    return (
        // chart height이 100%이기 때문이 chart를 덮는 마크업 요소에 height 설정
        <div style={{ width: '100%', height: '500px', margin: '0 auto' }}>
<ResponsiveLine
    colors={{ scheme: "dark2" }}
    data={e.data}
    margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
    xScale={{ type: "point" }}
    yScale={{
      type: "linear",
      min: "auto",
      max: "auto",
      stacked: true,
      reverse: false
    }}
    theme={{
        /**
         * label style (bar에 표현되는 글씨)
         */
        labels: {
            text: {
                fontSize: 14,
                fill: '#000000',
            },
        },
        /**
         * legend style (default로 우측 하단에 있는 색상별 key 표시)
         */
        legends: {
            text: {
                fontSize: 12,
                fill: '#000000',
            },
        },
        axis: {
            /**
             * axis legend style (bottom, left에 있는 글씨)
             */
            legend: {
                text: {
                    fontSize: 20,
                    fill: '#000000',
                },
            },
            /**
             * axis ticks style (bottom, left에 있는 값)
             */
            ticks: {
                text: {
                    fontSize: 16,
                    fill: '#000000',
                },
            },
        },
    }}
    axisTop={null}
    axisRight={null}
    axisBottom={{
      orient: "bottom",
      tickSize: 2,
      tickPadding: 5,
      tickRotation: -40,
      legendOffset: 40,
      legendPosition: "middle"
    }}
    axisLeft={{
      orient: "left",
      tickSize: 5,
      tickPadding: 5,
      tickRotation: 0,
      legendOffset: -50,
      legendPosition: "middle"
    }}
    pointSize={0}
    pointColor={{ theme: "background" }}
    pointBorderWidth={2}
    pointBorderColor="black"
    pointLabelYOffset={-12}
    useMesh={true}
    legends={[
      {
        anchor: "bottom-right",
        direction: "column",
        justify: false,
        translateX: 100,
        translateY: 0,
        itemsSpacing: 0,
        itemDirection: "left-to-right",
        itemWidth: 80,
        itemHeight: 20,
        itemOpacity: 0.75,
        symbolSize: 12,
        symbolShape: "circle",
        symbolBorderColor: "rgba(0, 0, 0, .5)",
        effects: [
          {
            on: "hover",
            style: {
              itemBackground: "rgba(0, 0, 0, .03)",
              itemOpacity: 1
            }
          }
        ]
      }
    ]}
  />
        </div>
    );
};

export default Barchart;