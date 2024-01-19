# combining scripting_example.py and operate_on_odb_1.py
# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import numpy as np
from abaqus import *
from abaqusConstants import *
import __main__
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
length_of_geom =np.array([1,2,3,4,5])
for i in length_of_geom:
    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    del mdb.models['Model-1'].sketches['__profile__']
    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=5.0)
    mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
        point2=(i, 1.0))
    mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type=
        DEFORMABLE_BODY)
    mdb.models['Model-1'].parts['Part-1'].BaseSolidExtrude(depth=1.0, sketch=
        mdb.models['Model-1'].sketches['__profile__'])
    del mdb.models['Model-1'].sketches['__profile__']
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].Elastic(table=((2000000000.0, 
        0.33), ))
    mdb.models['Model-1'].HomogeneousSolidSection(material='Material-1', name=
        'Section-1', thickness=None)
    mdb.models['Model-1'].parts['Part-1'].Set(cells=
        mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
        ), ), name='Set-1')
    mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
        offsetField='', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName=
        'Section-1', thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
        part=mdb.models['Model-1'].parts['Part-1'])
    mdb.models['Model-1'].StaticStep(initialInc=0.01, name='Step-1', nlgeom=ON, 
        previous='Initial')
    mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1, 
        minSizeFactor=0.1, size=i)
    mdb.models['Model-1'].parts['Part-1'].generateMesh()
    mdb.models['Model-1'].rootAssembly.regenerate()
    mdb.models['Model-1'].rootAssembly.Set(faces=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
        ('[#1 ]', ), ), name='Set-1')
    mdb.models['Model-1'].XsymmBC(createStepName='Step-1', localCsys=None, name=
        'BC-1', region=mdb.models['Model-1'].rootAssembly.sets['Set-1'])
    mdb.models['Model-1'].rootAssembly.Set(faces=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
        ('[#8 ]', ), ), name='Set-2')
    mdb.models['Model-1'].YsymmBC(createStepName='Step-1', localCsys=None, name=
        'BC-2', region=mdb.models['Model-1'].rootAssembly.sets['Set-2'])
    mdb.models['Model-1'].rootAssembly.Set(faces=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
        ('[#20 ]', ), ), name='Set-3')
    mdb.models['Model-1'].ZsymmBC(createStepName='Step-1', localCsys=None, name=
        'BC-3', region=mdb.models['Model-1'].rootAssembly.sets['Set-3'])
    mdb.models['Model-1'].rootAssembly.Set(faces=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
        ('[#4 ]', ), ), name='Set-4')
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
        distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
        'BC-4', region=mdb.models['Model-1'].rootAssembly.sets['Set-4'], u1=0.5, 
        u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
    job_name='mani_'+str(i)
    mdb.Job(name=job_name, model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
        numGPUs=0)
    mdb.jobs[job_name].submit(consistencyChecking=OFF)
    mdb.jobs[job_name].waitForCompletion() ##wait for the analysis to complete
# Operate on generated odb files
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
    # Try to get the XY plot, or create it if it doesn't exist
    try:
        xyp = session.xyPlots['XYPlot-1']
    except KeyError:
        print("XYPlot-1 does not exist. Creating it now.")
        xyp = session.XYPlot(name='XYPlot-1')
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
