import project3_output
import project3_api

def get_directions() -> str:
    '''
    User inputs the number of locations and the locations and
    the number of outputs and the outputs they want.
    '''

    #Checks to see if the number of locations is at least 2,
    #if not then the user will be prompted again.
    
    while True:
        num_locations = int(input(''))
        if num_locations < 2:
            print('Need at least 2 locations')
        else:
            break
        
    #After user inputs N number of locations, user will list out locations.
    #Only the first N locations will be taken in and stored in a list.
        
    locations = []
    for location in range(num_locations):
        location = input('')
        locations.append(location)
    
    #After taking in the locations, user will say how many outputs they want.
    #Must be at least 1, if not then user will be prompted again.
        
    while True:
        try:
            num_outputs = int(input(''))
            if num_outputs < 1:
                print('Must have at least 1 output')
            else:
                break
        except ValueError:
            print('Input the number of outputs you want.')

    #After user inputs O number of outputs, user will list out which outputs
    #they want. Only the first O outputs will be taken in and stored in a list.
    #Each input will be checked and an object from the designated will be
    #created.
        
    outputs = []
    for output in range(num_outputs):
        output = input('')
        if output == 'STEPS':
            outputs.append(project3_output.Steps())
        elif output == 'TOTALDISTANCE':
            outputs.append(project3_output.Distance())
        elif output == 'TOTALTIME':
            outputs.append(project3_output.Time())
        elif output == 'LATLONG':
            outputs.append(project3_output.LatitudeLongitude(num_locations))
        elif output == 'ELEVATION':
            outputs.append(project3_output.Elevation(num_locations))

    try:
        data = project3_api.get_result(project3_api.build_destination_url(locations))
        project3_output.run_outputs(outputs, data)
    except:
        project3_output.Error().output()
    
    
if __name__ == '__main__':
    get_directions()
