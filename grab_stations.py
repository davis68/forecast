import requests

def grab_website_data():
    '''Get raw data as HTML string from the NOAA website.'''
    url = 'http://www.nws.noaa.gov/mdl/gfslamp/docs/stations_info.shtml'
    pass  # YOUR CODE HERE

def extract_section(text):
    '''Find Illinois data segment (in a PRE tag).
    We know (from examination) that inside of the PRE block containing ' IL '
    (with whitespace and case matching) we can find the IL station data.
    This solution isn't robust, but it's good enough for practical cases.'''
    il_start  = text.find(' IL ')
    tag_start = text.rfind('PRE', il_start-200, il_start) # look backwards
    tag_end   = text.find('PRE', il_start)
    return text[tag_start+4:tag_end-2]

def parse_station_line(line):
    '''Extract latitude and longitude of stations. We know the columns are fixed
    (which is both inconvenient and convenient). In this case, we will simply
    set the limits of the relevant columns by counting the number of columns
    over we need to go.'''
    pass  # YOUR CODE HERE


text = grab_website_data()
data = extract_section(text)
for line in data.splitlines():
    try:
        stn, lat, lon = parse_station_line(line)
        print('%s\t%f\t%f'%(stn,lon,lat))
    except:
        pass
        #print('Could not parse line\n\t%s'%line)
