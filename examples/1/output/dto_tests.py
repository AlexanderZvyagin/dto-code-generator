
import sys, random, uuid
from output.dto import *

def random_string(len_max=5):
    return str(uuid.uuid4())[0:random.randint(0,len_max)]

def random_list_of_strings(min = 0, max = 3):
    n = random.randint(min,max)
    return [random_string() for i in range(n)]

def random_int (min = -1000, max = 1000):
    return random.randint(min,max)

def random_list_of_ints(min = 0, max = 3):
    n = random.randint(min,max)
    return [random_int() for i in range(n)]

def random_float (min = -1e6, max = 1e6):
    return random.uniform(min,max)

def random_list_of_floats (min = 0, max = 3):
    n = random.randint(min,max)
    return [random_float() for i in range(n)]


def random_UpdaterDoc ():
    return UpdaterDoc (
        random_string(),
        random_string(),
        random_string(),
        random_string(),
        random_int(),
        random_int()

    )


def random_list_of_UpdaterDoc (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_UpdaterDoc() for i in range(size)]


def random_UpdaterDto ():
    return UpdaterDto (
        random_string(),
        random_list_of_ints(),
        random_list_of_floats(),
        random_float()

    )


def random_list_of_UpdaterDto (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_UpdaterDto() for i in range(size)]


def random_Updater ():
    return Updater (
        random_string(),
        random_list_of_ints(),
        random_list_of_floats(),
        random_float()

    )


def random_list_of_Updater (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_Updater() for i in range(size)]


def random_IndependentGaussian ():
    return IndependentGaussian (
        random_list_of_ints()

    )


def random_list_of_IndependentGaussian (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_IndependentGaussian() for i in range(size)]


def random_CorrelatedGaussian ():
    return CorrelatedGaussian (
        random_float(),
        random_int(),
        random_int()

    )


def random_list_of_CorrelatedGaussian (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_CorrelatedGaussian() for i in range(size)]


def random_Barrier ():
    return Barrier (
        random_int(),
        random_float(),
        random_float(),
        random_int(),
        random_int(),
        random_float()

    )


def random_list_of_Barrier (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_Barrier() for i in range(size)]


def random_HistogramAxis ():
    return HistogramAxis (
        random_int(),
        random_int(),
        random_float(),
        random_float()

    )


def random_list_of_HistogramAxis (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_HistogramAxis() for i in range(size)]


def random_Histogram ():
    return Histogram (
        random_HistogramAxis(),
        random_HistogramAxis()

    )


def random_list_of_Histogram (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_Histogram() for i in range(size)]


def random_EvaluationPoint ():
    return EvaluationPoint (
        random_int(),
        random_float(),
        random_float(),
        random_float()

    )


def random_list_of_EvaluationPoint (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_EvaluationPoint() for i in range(size)]


def random_EvaluationResults ():
    return EvaluationResults (
        random_list_of_strings(),
        random_list_of_ints(),
        random_list_of_floats(),
        random_list_of_floats(),
        random_list_of_floats(),
        random_list_of_floats(),
        random_list_of_ints(),
        random_list_of_Histogram()

    )


def random_list_of_EvaluationResults (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_EvaluationResults() for i in range(size)]


def random_Parameter ():
    return Parameter (
        random_float(),
        random_float(),
        random_float(),
        random_float()

    )


def random_list_of_Parameter (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_Parameter() for i in range(size)]


def random_Model ():
    return Model (
        random_float(),
        random_int(),
        random_int(),
        random_list_of_Updater(),
        random_list_of_EvaluationPoint(),
        random_float(),
        random_int()

    )


def random_list_of_Model (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_Model() for i in range(size)]


def test_round_trip_python(command, struct_name, file1_name, file2_name):
    if command=='build':
        return

    if command=='create':
        if False:
            pass

        elif struct_name=='UpdaterDoc':
            obj = UpdaterDoc_to_json_string(random_UpdaterDoc())
            open(file1_name,'w').write(obj)


        elif struct_name=='UpdaterDto':
            obj = UpdaterDto_to_json_string(random_UpdaterDto())
            open(file1_name,'w').write(obj)


        elif struct_name=='Updater':
            obj = Updater_to_json_string(random_Updater())
            open(file1_name,'w').write(obj)


        elif struct_name=='IndependentGaussian':
            obj = IndependentGaussian_to_json_string(random_IndependentGaussian())
            open(file1_name,'w').write(obj)


        elif struct_name=='CorrelatedGaussian':
            obj = CorrelatedGaussian_to_json_string(random_CorrelatedGaussian())
            open(file1_name,'w').write(obj)


        elif struct_name=='Barrier':
            obj = Barrier_to_json_string(random_Barrier())
            open(file1_name,'w').write(obj)


        elif struct_name=='HistogramAxis':
            obj = HistogramAxis_to_json_string(random_HistogramAxis())
            open(file1_name,'w').write(obj)


        elif struct_name=='Histogram':
            obj = Histogram_to_json_string(random_Histogram())
            open(file1_name,'w').write(obj)


        elif struct_name=='EvaluationPoint':
            obj = EvaluationPoint_to_json_string(random_EvaluationPoint())
            open(file1_name,'w').write(obj)


        elif struct_name=='EvaluationResults':
            obj = EvaluationResults_to_json_string(random_EvaluationResults())
            open(file1_name,'w').write(obj)


        elif struct_name=='Parameter':
            obj = Parameter_to_json_string(random_Parameter())
            open(file1_name,'w').write(obj)


        elif struct_name=='Model':
            obj = Model_to_json_string(random_Model())
            open(file1_name,'w').write(obj)

        else:
            raise Exception(f'Operation "{command}" does not supported struct {struct_name}')
    elif command=='convert':
        if False:
            pass

        elif struct_name=='UpdaterDoc':
            obj = UpdaterDoc_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(UpdaterDoc_to_json_string(obj))


        elif struct_name=='UpdaterDto':
            obj = UpdaterDto_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(UpdaterDto_to_json_string(obj))


        elif struct_name=='Updater':
            obj = Updater_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Updater_to_json_string(obj))


        elif struct_name=='IndependentGaussian':
            obj = IndependentGaussian_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(IndependentGaussian_to_json_string(obj))


        elif struct_name=='CorrelatedGaussian':
            obj = CorrelatedGaussian_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(CorrelatedGaussian_to_json_string(obj))


        elif struct_name=='Barrier':
            obj = Barrier_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Barrier_to_json_string(obj))


        elif struct_name=='HistogramAxis':
            obj = HistogramAxis_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(HistogramAxis_to_json_string(obj))


        elif struct_name=='Histogram':
            obj = Histogram_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Histogram_to_json_string(obj))


        elif struct_name=='EvaluationPoint':
            obj = EvaluationPoint_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(EvaluationPoint_to_json_string(obj))


        elif struct_name=='EvaluationResults':
            obj = EvaluationResults_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(EvaluationResults_to_json_string(obj))


        elif struct_name=='Parameter':
            obj = Parameter_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Parameter_to_json_string(obj))


        elif struct_name=='Model':
            obj = Model_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Model_to_json_string(obj))

        else:
            raise Exception(f'Operation "{command}" does not supported struct {struct_name}')
    elif command=='compare':
        if False:
            pass

        elif struct_name=='UpdaterDoc':
            obj1 = UpdaterDoc_from_json_string(open(file1_name).read())
            obj2 = UpdaterDoc_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='UpdaterDto':
            obj1 = UpdaterDto_from_json_string(open(file1_name).read())
            obj2 = UpdaterDto_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='Updater':
            obj1 = Updater_from_json_string(open(file1_name).read())
            obj2 = Updater_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='IndependentGaussian':
            obj1 = IndependentGaussian_from_json_string(open(file1_name).read())
            obj2 = IndependentGaussian_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='CorrelatedGaussian':
            obj1 = CorrelatedGaussian_from_json_string(open(file1_name).read())
            obj2 = CorrelatedGaussian_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='Barrier':
            obj1 = Barrier_from_json_string(open(file1_name).read())
            obj2 = Barrier_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='HistogramAxis':
            obj1 = HistogramAxis_from_json_string(open(file1_name).read())
            obj2 = HistogramAxis_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='Histogram':
            obj1 = Histogram_from_json_string(open(file1_name).read())
            obj2 = Histogram_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='EvaluationPoint':
            obj1 = EvaluationPoint_from_json_string(open(file1_name).read())
            obj2 = EvaluationPoint_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='EvaluationResults':
            obj1 = EvaluationResults_from_json_string(open(file1_name).read())
            obj2 = EvaluationResults_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='Parameter':
            obj1 = Parameter_from_json_string(open(file1_name).read())
            obj2 = Parameter_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='Model':
            obj1 = Model_from_json_string(open(file1_name).read())
            obj2 = Model_from_json_string(open(file2_name).read())
            assert obj1==obj2

        else:
            raise Exception(f'Operation "{command}" does not supported struct {struct_name}')
    else:
        raise Exception(f'Not supported command {command}')

