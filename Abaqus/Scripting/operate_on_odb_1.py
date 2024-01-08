# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
for i in range(1,6):
    odb_name='mani_'+str(i)+'.odb'
    o1 = session.openOdb(
        name='C:/Users/arvin/Documents/Mani/Abaqus/Scripting/Linear Elastic/'+odb_name)
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    odb = session.odbs['C:/Users/arvin/Documents/Mani/Abaqus/Scripting/Linear Elastic/'+odb_name]
    xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
        variable=(('LE', INTEGRATION_POINT, ((COMPONENT, 'LE11'), )), ('S', 
        INTEGRATION_POINT, ((COMPONENT, 'S11'), )), ), elementPick=((
        'PART-1-1', 1, ('[#1 ]', )), ), )
    xyp = session.xyPlots['XYPlot-1']
    chartName = xyp.charts.keys()[0]
    chart = xyp.charts[chartName]
    curveList = session.curveSet(xyData=xyList)
    chart.setValues(curvesToPlot=curveList)
    session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
    xy1 = session.xyDataObjects['_LE:LE11 PI: PART-1-1 E: 1 IP: 1']
    xy2 = session.xyDataObjects['_S:S11 PI: PART-1-1 E: 1 IP: 1']
    xy3 = combine(xy1, xy2)
    xyp = session.xyPlots['XYPlot-1']
    chartName = xyp.charts.keys()[0]
    chart = xyp.charts[chartName]
    c1 = session.Curve(xyData=xy3)
    chart.setValues(curvesToPlot=(c1, ), )
    f_name='mani_'+str(i)
    session.printToFile(fileName=f_name, format=TIFF, canvasObjects=(
        session.viewports['Viewport: 1'], ))
    session.printToFile(fileName=f_name, format=TIFF, canvasObjects=(
        session.viewports['Viewport: 1'], ))

