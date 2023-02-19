
import sys, random, uuid
from output.dto import *

def random_string(len_max=5):
    return str(uuid.uuid4())[0:random.randint(0,len_max)]

def random_list_string(min = 0, max = 3):
    n = random.randint(min,max)
    return [random_string() for i in range(n)]

def random_int (min = -1000, max = 1000):
    return random.randint(min,max)

def random_list_int(min = 0, max = 3):
    n = random.randint(min,max)
    return [random_int() for i in range(n)]

def random_optional_list_int(min = 0, max = 3):
    if random.randint(0,1): return None
    n = random.randint(min,max)
    return [random_int() for i in range(n)]

def random_float (min = -1e6, max = 1e6):
    return random_int()
    # FIXME
    # return random.uniform(min,max)

def random_optional_float (min = -1e6, max = 1e6):
    if random.randint(0,1): return None
    return random_int()
    # FIXME
    # return random.uniform(min,max)

def random_list_float (min = 0, max = 3):
    n = random.randint(min,max)
    return [random_float() for i in range(n)]

def random_optional_list_float (min = 0, max = 3):
    if random.randint(0,1): return None
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


def random_list_UpdaterDoc (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_UpdaterDoc() for i in range(size)]


def random_UpdaterDto ():
    return UpdaterDto (
        random_string(),
        random_optional_list_int(),
        random_optional_list_float(),
        random_optional_float()

    )


def random_list_UpdaterDto (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_UpdaterDto() for i in range(size)]


def random_Updater ():
    return Updater (
        random_string(),
        random_list_int(),
        random_list_float(),
        random_float()

    )


def random_list_Updater (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_Updater() for i in range(size)]


def random_IndependentGaussian ():
    return IndependentGaussian (
        random_list_int()

    )


def random_list_IndependentGaussian (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_IndependentGaussian() for i in range(size)]


def random_CorrelatedGaussian ():
    return CorrelatedGaussian (
        random_float(),
        random_int(),
        random_int()

    )


def random_list_CorrelatedGaussian (min:int = 0, max:int = 3):
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


def random_list_Barrier (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_Barrier() for i in range(size)]


def random_HistogramAxis ():
    return HistogramAxis (
        random_int(),
        random_int(),
        random_float(),
        random_float()

    )


def random_list_HistogramAxis (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_HistogramAxis() for i in range(size)]


def random_Histogram ():
    return Histogram (
        random_HistogramAxis(),
        random_HistogramAxis()

    )


def random_list_Histogram (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_Histogram() for i in range(size)]


def random_EvaluationPoint ():
    return EvaluationPoint (
        random_int(),
        random_float(),
        random_float(),
        random_float()

    )


def random_list_EvaluationPoint (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_EvaluationPoint() for i in range(size)]


def random_EvaluationResults ():
    return EvaluationResults (
        random_list_string(),
        random_list_int(),
        random_list_float(),
        random_list_float(),
        random_list_float(),
        random_list_float(),
        random_list_int(),
        random_list_Histogram()

    )


def random_list_EvaluationResults (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_EvaluationResults() for i in range(size)]


def random_Parameter ():
    return Parameter (
        random_float(),
        random_float(),
        random_float(),
        random_float()

    )


def random_list_Parameter (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_Parameter() for i in range(size)]


def random_Model ():
    return Model (
        random_float(),
        random_int(),
        random_int(),
        random_list_Updater(),
        random_list_EvaluationPoint(),
        random_float(),
        random_int()

    )


def random_list_Model (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_Model() for i in range(size)]


def test_round_trip_python(command, struct_name, file1_name, file2_name):
    if command=='build':
        return

    if command=='create':
        if False:
            pass

        elif struct_name=='UpdaterDoc':
            obj1 = random_UpdaterDoc()
            open(file1_name,'w').write(UpdaterDoc_to_json_string(obj1))
            obj2 = UpdaterDoc_from_json_string(open(file1_name).read())
            assert isinstance(obj1,UpdaterDoc)
            assert isinstance(obj2,UpdaterDoc)
            assert obj1==obj2


        elif struct_name=='UpdaterDto':
            obj1 = random_UpdaterDto()
            open(file1_name,'w').write(UpdaterDto_to_json_string(obj1))
            obj2 = UpdaterDto_from_json_string(open(file1_name).read())
            assert isinstance(obj1,UpdaterDto)
            assert isinstance(obj2,UpdaterDto)
            assert obj1==obj2


        elif struct_name=='Updater':
            obj1 = random_Updater()
            open(file1_name,'w').write(Updater_to_json_string(obj1))
            obj2 = Updater_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Updater)
            assert isinstance(obj2,Updater)
            assert obj1==obj2


        elif struct_name=='IndependentGaussian':
            obj1 = random_IndependentGaussian()
            open(file1_name,'w').write(IndependentGaussian_to_json_string(obj1))
            obj2 = IndependentGaussian_from_json_string(open(file1_name).read())
            assert isinstance(obj1,IndependentGaussian)
            assert isinstance(obj2,IndependentGaussian)
            assert obj1==obj2


        elif struct_name=='CorrelatedGaussian':
            obj1 = random_CorrelatedGaussian()
            open(file1_name,'w').write(CorrelatedGaussian_to_json_string(obj1))
            obj2 = CorrelatedGaussian_from_json_string(open(file1_name).read())
            assert isinstance(obj1,CorrelatedGaussian)
            assert isinstance(obj2,CorrelatedGaussian)
            assert obj1==obj2


        elif struct_name=='Barrier':
            obj1 = random_Barrier()
            open(file1_name,'w').write(Barrier_to_json_string(obj1))
            obj2 = Barrier_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Barrier)
            assert isinstance(obj2,Barrier)
            assert obj1==obj2


        elif struct_name=='HistogramAxis':
            obj1 = random_HistogramAxis()
            open(file1_name,'w').write(HistogramAxis_to_json_string(obj1))
            obj2 = HistogramAxis_from_json_string(open(file1_name).read())
            assert isinstance(obj1,HistogramAxis)
            assert isinstance(obj2,HistogramAxis)
            assert obj1==obj2


        elif struct_name=='Histogram':
            obj1 = random_Histogram()
            open(file1_name,'w').write(Histogram_to_json_string(obj1))
            obj2 = Histogram_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Histogram)
            assert isinstance(obj2,Histogram)
            assert obj1==obj2


        elif struct_name=='EvaluationPoint':
            obj1 = random_EvaluationPoint()
            open(file1_name,'w').write(EvaluationPoint_to_json_string(obj1))
            obj2 = EvaluationPoint_from_json_string(open(file1_name).read())
            assert isinstance(obj1,EvaluationPoint)
            assert isinstance(obj2,EvaluationPoint)
            assert obj1==obj2


        elif struct_name=='EvaluationResults':
            obj1 = random_EvaluationResults()
            open(file1_name,'w').write(EvaluationResults_to_json_string(obj1))
            obj2 = EvaluationResults_from_json_string(open(file1_name).read())
            assert isinstance(obj1,EvaluationResults)
            assert isinstance(obj2,EvaluationResults)
            assert obj1==obj2


        elif struct_name=='Parameter':
            obj1 = random_Parameter()
            open(file1_name,'w').write(Parameter_to_json_string(obj1))
            obj2 = Parameter_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Parameter)
            assert isinstance(obj2,Parameter)
            assert obj1==obj2


        elif struct_name=='Model':
            obj1 = random_Model()
            open(file1_name,'w').write(Model_to_json_string(obj1))
            obj2 = Model_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Model)
            assert isinstance(obj2,Model)
            assert obj1==obj2

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

