# -*- coding: utf-8 -*-
"""
Highcharts Demos
Basic line: http://www.highcharts.com/demo/line-basic
"""
from highcharts_excentis import Highchart
H = Highchart()

data_Tokyo = [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
data_NY = [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
data_Berlin = [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
data_London = [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]

H.add_data_set(data_Tokyo, 'line', 'Tokyo')
H.add_data_set(data_NY, 'line', 'New York')
H.add_data_set(data_Berlin, 'line', 'Berlin')
H.add_data_set(data_London, 'line', 'London')

H.set_options('chart', {'zoomType': 'x'})
H.set_options('xAxis', {'categories': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
	'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']})

H.set_options('yAxis',{ 'title': { 'text': 'Temperature (°C)'},
            'plotLines': {'value': 0, 'width': 1, 'color': '#808080'}})
H.set_options('tooltip', {'valueSuffix': '°C'})

H.set_options('legend', {'layout': 'vertical','align': 'right',
	'verticalAlign': 'middle','borderWidth': 0})
H.set_options('colors',{})
H.set_options('plotOptions',{'line': {
                'dataLabels': {
                    'enabled': True
                }}})

H.htmlcontent