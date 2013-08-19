# example_csw_ngdc_geoportal
# Obtain ISO queryables thru ESRI Geoportal CSW using OWSLIB
#
#
# Using usage examples from http://geopython.github.io/OWSLib/#csw
# and Rich Signell example http://nbviewer.ipython.org/5769439
#

from owslib.csw import CatalogueServiceWeb
from owslib import fes

from IPython.core.display import HTML
HTML('<iframe src=http://geoport.whoi.edu/geoportal/ width=950 height=400></iframe>')
endpoint = 'http://www.ngdc.noaa.gov/geoportal/csw' 

csw = CatalogueServiceWeb(endpoint,timeout=30)
csw.version

[op.name for op in csw.operations]

csw.getrecords(keywords=['sea_water_temperature'], maxrecords=20)
csw.results

csw.records[rec].title

for rec in csw.records:
     print csw.records[rec].title

# ------------------------------------------------------------------
# Rich Signell example http://nbviewer.ipython.org/5769439
# what owslib I installed does not have the same functions for fes as Rich's code

# hopefully something like this will be implemented in fes soon 
def dateRange(start_date='1900-01-01',stop_date='2100-01-01',constraint='overlaps'):
    if constraint == 'overlaps':
        start = fes.PropertyIsLessThanOrEqualTo(propertyname='startDate', literal=stop_date)
        stop = fes.PropertyIsGreaterThanOrEqualTo(propertyname='endDate', literal=start_date)
    elif constraint == 'within':
        start = fes.PropertyIsGreaterThanOrEqualTo(propertyname='startDate', literal=start_date)
        stop = fes.PropertyIsLessThanOrEqualTo(propertyname='endDate', literal=stop_date)
    return start,stop

# Perform the CSW query, using Kyle's cool new filters on ISO queryables
# find all datasets in a bounding box and temporal extent that have 
# specific keywords and also can be accessed via OPeNDAP  

bbox = fes.BBox([-71.5, 39.5, -63.0, 46])
start,stop = dateRange('1970-01-01','1979-02-01')
std_name = 'sea_water_temperature'
keywords = fes.PropertyIsLike(propertyname='anyText', literal=std_name)
serviceType = fes.PropertyIsLike(propertyname='apiso:ServiceType', literal='*opendap*')

# apply all the filters using the "and" syntax: [[filter1,filter2]]
csw.getrecords2(constraints=[[keywords,start,stop,serviceType,bbox]],maxrecords=3,esn='full')
csw.records.keys()
