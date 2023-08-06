import picos as picos_interface

def Get(model_object, result, input1, input2=None):
   
   input1 = input1[0]

   match input1:
      
    case 'variable':
        
        return input2.value
    
    case 'status':

        return result[0].claimedStatus
         
    case 'objective':

        return model_object.obj_value()

    case 'time':

        return (result[1][1]-result[1][0])