
// This file was automatically generated!
// - by <software> <version>
// - from <DTO-s spec>

import * as fs from 'fs'

import * as dto from './dto'
import {
    UpdaterDoc,
    UpdaterDto,
    Updater,
    IndependentGaussian,
    CorrelatedGaussian,
    Barrier,
    HistogramAxis,
    Histogram,
    EvaluationPoint,
    EvaluationResults,
    Parameter,
    Model,
} from './dto'

function random_int(min:number = -1000, max:number = 1000) : number {
    return Math.floor (min + Math.random()*(max-min+1));
}

function yes_no () : boolean {
    return random_int(0,1)==1;
}

function random_optional_int() : number|undefined {
    return yes_no() ? random_int() : undefined;
}

function random_float(min:number = -1e6, max:number = 1e6) : number {
    return random_int();
}

function random_optional_float() : number|undefined {
    return yes_no() ? random_float() : undefined;
}

function random_string(min:number = 0, max:number = 3) : string {
    let out: string = '';
    const input: string = 'abcdefghijklmnopqrstuvwxyz0123456789';
    for (let i = 0; i < 32; i++)
        out += input.charAt(random_int(0,input.length));
    return out;
}

function random_optional_string() : string|undefined {
    return yes_no() ? random_string() : undefined;
}

function random_list_int (min:number = 0, max:number = 3) : number[] {
    const size = random_int(min,max);
    let list:number[] = [];
    for(let i=0; i<size; i++)
        list.push(random_int());
    return list;
}

function random_optional_list_int() : number[]|undefined {
    return yes_no() ? random_list_int() : undefined;
}

function random_list_float (min:number = 0, max:number = 3) : number[] {
    const size = random_int(min,max);
    let list:number[] = [];
    for(let i=0; i<size; i++)
        list.push(random_float());
    return list;
}

function random_optional_list_float() : number[]|undefined {
    return yes_no() ? random_list_float() : undefined;
}

function random_list_string (min:number = 0, max:number = 3) : string[] {
    const size = random_int(min,max);
    let list:string[] = [];
    for(let i=0; i<size; i++)
        list.push(random_string());
    return list;
}

function random_optional_list_string() : string[]|undefined {
    return yes_no() ? random_list_string() : undefined;
}

// https://stackoverflow.com/questions/1068834/object-comparison-in-javascript/6713782#6713782
// function object_equals( x, y ) {
//     if ( x === y ) return true;
//       // if both x and y are null or undefined and exactly the same
//   
//     if ( ! ( x instanceof Object ) || ! ( y instanceof Object ) ) return false;
//       // if they are not strictly equal, they both need to be Objects
//   
//     if ( x.constructor !== y.constructor ) return false;
//       // they must have the exact same prototype chain, the closest we can do is
//       // test there constructor.
//   
//     for ( var p in x ) {
//       if ( ! x.hasOwnProperty( p ) ) continue;
//         // other properties were tested using x.constructor === y.constructor
//   
//       if ( ! y.hasOwnProperty( p ) ) return false;
//         // allows to compare x[ p ] and y[ p ] when set to undefined
//   
//       if ( x[ p ] === y[ p ] ) continue;
//         // if they have the same strict value or identity then they are equal
//   
//       if ( typeof( x[ p ] ) !== "object" ) return false;
//         // Numbers, Strings, Functions, Booleans must be strictly equal
//   
//       if ( ! object_equals( x[ p ],  y[ p ] ) ) return false;
//         // Objects and Arrays must be tested recursively
//     }
//   
//     for ( p in y )
//       if ( y.hasOwnProperty( p ) && ! x.hasOwnProperty( p ) )
//         return false;
//           // allows x[ p ] to be set to undefined
//   
//     return true;
// }


function random_UpdaterDoc () : UpdaterDoc {
    return new UpdaterDoc (
        random_string(),
        random_string(),
        random_string(),
        random_string(),
        random_int(),
        random_int()

    );
}


function random_list_UpdaterDoc (min:number = 0, max:number = 3) : UpdaterDoc[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:UpdaterDoc[] = [];
    for(let i=0; i<size; i++)
        list.push(random_UpdaterDoc());
    return list;
}


function random_UpdaterDto () : UpdaterDto {
    return new UpdaterDto (
        random_string(),
        random_optional_list_int(),
        random_optional_list_float(),
        random_optional_float()

    );
}


function random_list_UpdaterDto (min:number = 0, max:number = 3) : UpdaterDto[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:UpdaterDto[] = [];
    for(let i=0; i<size; i++)
        list.push(random_UpdaterDto());
    return list;
}


function random_Updater () : Updater {
    return new Updater (
        random_string(),
        random_list_int(),
        random_list_float(),
        random_float()

    );
}


function random_list_Updater (min:number = 0, max:number = 3) : Updater[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Updater[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Updater());
    return list;
}


function random_IndependentGaussian () : IndependentGaussian {
    return new IndependentGaussian (
        random_list_int()

    );
}


function random_list_IndependentGaussian (min:number = 0, max:number = 3) : IndependentGaussian[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:IndependentGaussian[] = [];
    for(let i=0; i<size; i++)
        list.push(random_IndependentGaussian());
    return list;
}


function random_CorrelatedGaussian () : CorrelatedGaussian {
    return new CorrelatedGaussian (
        random_float(),
        random_int(),
        random_int()

    );
}


function random_list_CorrelatedGaussian (min:number = 0, max:number = 3) : CorrelatedGaussian[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:CorrelatedGaussian[] = [];
    for(let i=0; i<size; i++)
        list.push(random_CorrelatedGaussian());
    return list;
}


function random_Barrier () : Barrier {
    return new Barrier (
        random_int(),
        random_float(),
        random_float(),
        random_int(),
        random_int(),
        random_float()

    );
}


function random_list_Barrier (min:number = 0, max:number = 3) : Barrier[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Barrier[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Barrier());
    return list;
}


function random_HistogramAxis () : HistogramAxis {
    return new HistogramAxis (
        random_int(),
        random_int(),
        random_float(),
        random_float()

    );
}


function random_list_HistogramAxis (min:number = 0, max:number = 3) : HistogramAxis[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:HistogramAxis[] = [];
    for(let i=0; i<size; i++)
        list.push(random_HistogramAxis());
    return list;
}


function random_Histogram () : Histogram {
    return new Histogram (
        random_HistogramAxis(),
        random_HistogramAxis()

    );
}


function random_list_Histogram (min:number = 0, max:number = 3) : Histogram[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Histogram[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Histogram());
    return list;
}


function random_EvaluationPoint () : EvaluationPoint {
    return new EvaluationPoint (
        random_int(),
        random_float(),
        random_float(),
        random_float()

    );
}


function random_list_EvaluationPoint (min:number = 0, max:number = 3) : EvaluationPoint[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:EvaluationPoint[] = [];
    for(let i=0; i<size; i++)
        list.push(random_EvaluationPoint());
    return list;
}


function random_EvaluationResults () : EvaluationResults {
    return new EvaluationResults (
        random_list_string(),
        random_list_int(),
        random_list_float(),
        random_list_float(),
        random_list_float(),
        random_list_float(),
        random_list_int(),
        random_list_Histogram()

    );
}


function random_list_EvaluationResults (min:number = 0, max:number = 3) : EvaluationResults[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:EvaluationResults[] = [];
    for(let i=0; i<size; i++)
        list.push(random_EvaluationResults());
    return list;
}


function random_Parameter () : Parameter {
    return new Parameter (
        random_float(),
        random_float(),
        random_float(),
        random_float()

    );
}


function random_list_Parameter (min:number = 0, max:number = 3) : Parameter[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Parameter[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Parameter());
    return list;
}


function random_Model () : Model {
    return new Model (
        random_float(),
        random_int(),
        random_int(),
        random_list_Updater(),
        random_list_EvaluationPoint(),
        random_float(),
        random_int()

    );
}


function random_list_Model (min:number = 0, max:number = 3) : Model[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Model[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Model());
    return list;
}


function create (struct_name:string, file_name:string){
    if(false){

    } else if (struct_name === 'UpdaterDoc') {
        const obj1: UpdaterDoc = random_UpdaterDoc();
        const j: object = {};
        dto.UpdaterDoc_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        // const j = JSON.parse(fs.readFileSync(file_name,'utf-8'));
        const obj2: UpdaterDoc = new UpdaterDoc();
        dto.UpdaterDoc_from_json(j,obj2);
        // const jstr: string = fs.readFileSync(file_name,'utf-8');
        // const obj2: UpdaterDoc = dto.UpdaterDoc_fromJSON_string(jstr);
        if(!dto.UpdaterDoc_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'UpdaterDto') {
        const obj1: UpdaterDto = random_UpdaterDto();
        const j: object = {};
        dto.UpdaterDto_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        // const j = JSON.parse(fs.readFileSync(file_name,'utf-8'));
        const obj2: UpdaterDto = new UpdaterDto();
        dto.UpdaterDto_from_json(j,obj2);
        // const jstr: string = fs.readFileSync(file_name,'utf-8');
        // const obj2: UpdaterDto = dto.UpdaterDto_fromJSON_string(jstr);
        if(!dto.UpdaterDto_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Updater') {
        const obj1: Updater = random_Updater();
        const j: object = {};
        dto.Updater_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        // const j = JSON.parse(fs.readFileSync(file_name,'utf-8'));
        const obj2: Updater = new Updater();
        dto.Updater_from_json(j,obj2);
        // const jstr: string = fs.readFileSync(file_name,'utf-8');
        // const obj2: Updater = dto.Updater_fromJSON_string(jstr);
        if(!dto.Updater_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'IndependentGaussian') {
        const obj1: IndependentGaussian = random_IndependentGaussian();
        const j: object = {};
        dto.IndependentGaussian_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        // const j = JSON.parse(fs.readFileSync(file_name,'utf-8'));
        const obj2: IndependentGaussian = new IndependentGaussian();
        dto.IndependentGaussian_from_json(j,obj2);
        // const jstr: string = fs.readFileSync(file_name,'utf-8');
        // const obj2: IndependentGaussian = dto.IndependentGaussian_fromJSON_string(jstr);
        if(!dto.IndependentGaussian_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'CorrelatedGaussian') {
        const obj1: CorrelatedGaussian = random_CorrelatedGaussian();
        const j: object = {};
        dto.CorrelatedGaussian_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        // const j = JSON.parse(fs.readFileSync(file_name,'utf-8'));
        const obj2: CorrelatedGaussian = new CorrelatedGaussian();
        dto.CorrelatedGaussian_from_json(j,obj2);
        // const jstr: string = fs.readFileSync(file_name,'utf-8');
        // const obj2: CorrelatedGaussian = dto.CorrelatedGaussian_fromJSON_string(jstr);
        if(!dto.CorrelatedGaussian_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Barrier') {
        const obj1: Barrier = random_Barrier();
        const j: object = {};
        dto.Barrier_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        // const j = JSON.parse(fs.readFileSync(file_name,'utf-8'));
        const obj2: Barrier = new Barrier();
        dto.Barrier_from_json(j,obj2);
        // const jstr: string = fs.readFileSync(file_name,'utf-8');
        // const obj2: Barrier = dto.Barrier_fromJSON_string(jstr);
        if(!dto.Barrier_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'HistogramAxis') {
        const obj1: HistogramAxis = random_HistogramAxis();
        const j: object = {};
        dto.HistogramAxis_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        // const j = JSON.parse(fs.readFileSync(file_name,'utf-8'));
        const obj2: HistogramAxis = new HistogramAxis();
        dto.HistogramAxis_from_json(j,obj2);
        // const jstr: string = fs.readFileSync(file_name,'utf-8');
        // const obj2: HistogramAxis = dto.HistogramAxis_fromJSON_string(jstr);
        if(!dto.HistogramAxis_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Histogram') {
        const obj1: Histogram = random_Histogram();
        const j: object = {};
        dto.Histogram_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        // const j = JSON.parse(fs.readFileSync(file_name,'utf-8'));
        const obj2: Histogram = new Histogram();
        dto.Histogram_from_json(j,obj2);
        // const jstr: string = fs.readFileSync(file_name,'utf-8');
        // const obj2: Histogram = dto.Histogram_fromJSON_string(jstr);
        if(!dto.Histogram_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'EvaluationPoint') {
        const obj1: EvaluationPoint = random_EvaluationPoint();
        const j: object = {};
        dto.EvaluationPoint_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        // const j = JSON.parse(fs.readFileSync(file_name,'utf-8'));
        const obj2: EvaluationPoint = new EvaluationPoint();
        dto.EvaluationPoint_from_json(j,obj2);
        // const jstr: string = fs.readFileSync(file_name,'utf-8');
        // const obj2: EvaluationPoint = dto.EvaluationPoint_fromJSON_string(jstr);
        if(!dto.EvaluationPoint_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'EvaluationResults') {
        const obj1: EvaluationResults = random_EvaluationResults();
        const j: object = {};
        dto.EvaluationResults_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        // const j = JSON.parse(fs.readFileSync(file_name,'utf-8'));
        const obj2: EvaluationResults = new EvaluationResults();
        dto.EvaluationResults_from_json(j,obj2);
        // const jstr: string = fs.readFileSync(file_name,'utf-8');
        // const obj2: EvaluationResults = dto.EvaluationResults_fromJSON_string(jstr);
        if(!dto.EvaluationResults_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Parameter') {
        const obj1: Parameter = random_Parameter();
        const j: object = {};
        dto.Parameter_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        // const j = JSON.parse(fs.readFileSync(file_name,'utf-8'));
        const obj2: Parameter = new Parameter();
        dto.Parameter_from_json(j,obj2);
        // const jstr: string = fs.readFileSync(file_name,'utf-8');
        // const obj2: Parameter = dto.Parameter_fromJSON_string(jstr);
        if(!dto.Parameter_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Model') {
        const obj1: Model = random_Model();
        const j: object = {};
        dto.Model_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        // const j = JSON.parse(fs.readFileSync(file_name,'utf-8'));
        const obj2: Model = new Model();
        dto.Model_from_json(j,obj2);
        // const jstr: string = fs.readFileSync(file_name,'utf-8');
        // const obj2: Model = dto.Model_fromJSON_string(jstr);
        if(!dto.Model_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);

    } else
        throw new Error(`Cannot create an object of the structure ${struct_name}.`);
}

function convert (struct_name:string, file1_name:string, file2_name:string){
    if(false){

    } else if (struct_name === 'UpdaterDoc') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: UpdaterDoc = dto.UpdaterDoc_fromJSON_string(jstr);
        // fs.writeFileSync(file2_name, obj.toJSON());
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'UpdaterDto') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: UpdaterDto = dto.UpdaterDto_fromJSON_string(jstr);
        // fs.writeFileSync(file2_name, obj.toJSON());
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Updater') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Updater = dto.Updater_fromJSON_string(jstr);
        // fs.writeFileSync(file2_name, obj.toJSON());
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'IndependentGaussian') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: IndependentGaussian = dto.IndependentGaussian_fromJSON_string(jstr);
        // fs.writeFileSync(file2_name, obj.toJSON());
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'CorrelatedGaussian') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: CorrelatedGaussian = dto.CorrelatedGaussian_fromJSON_string(jstr);
        // fs.writeFileSync(file2_name, obj.toJSON());
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Barrier') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Barrier = dto.Barrier_fromJSON_string(jstr);
        // fs.writeFileSync(file2_name, obj.toJSON());
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'HistogramAxis') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: HistogramAxis = dto.HistogramAxis_fromJSON_string(jstr);
        // fs.writeFileSync(file2_name, obj.toJSON());
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Histogram') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Histogram = dto.Histogram_fromJSON_string(jstr);
        // fs.writeFileSync(file2_name, obj.toJSON());
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'EvaluationPoint') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: EvaluationPoint = dto.EvaluationPoint_fromJSON_string(jstr);
        // fs.writeFileSync(file2_name, obj.toJSON());
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'EvaluationResults') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: EvaluationResults = dto.EvaluationResults_fromJSON_string(jstr);
        // fs.writeFileSync(file2_name, obj.toJSON());
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Parameter') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Parameter = dto.Parameter_fromJSON_string(jstr);
        // fs.writeFileSync(file2_name, obj.toJSON());
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Model') {
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: Model = dto.Model_fromJSON_string(jstr);
        // fs.writeFileSync(file2_name, obj.toJSON());
        fs.writeFileSync(file2_name, JSON.stringify(obj));

    } else
        throw new Error(`Cannot convert an object of the structure ${struct_name}.`);
}

function compare (struct_name:string, file1_name:string, file2_name:string){
    if(false){

    } else if (struct_name === 'UpdaterDoc') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: UpdaterDoc = dto.UpdaterDoc_fromJSON_string(jstr1);
        const obj2: UpdaterDoc = dto.UpdaterDoc_fromJSON_string(jstr2);
        if(!dto.UpdaterDoc_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'UpdaterDto') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: UpdaterDto = dto.UpdaterDto_fromJSON_string(jstr1);
        const obj2: UpdaterDto = dto.UpdaterDto_fromJSON_string(jstr2);
        if(!dto.UpdaterDto_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Updater') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Updater = dto.Updater_fromJSON_string(jstr1);
        const obj2: Updater = dto.Updater_fromJSON_string(jstr2);
        if(!dto.Updater_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'IndependentGaussian') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: IndependentGaussian = dto.IndependentGaussian_fromJSON_string(jstr1);
        const obj2: IndependentGaussian = dto.IndependentGaussian_fromJSON_string(jstr2);
        if(!dto.IndependentGaussian_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'CorrelatedGaussian') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: CorrelatedGaussian = dto.CorrelatedGaussian_fromJSON_string(jstr1);
        const obj2: CorrelatedGaussian = dto.CorrelatedGaussian_fromJSON_string(jstr2);
        if(!dto.CorrelatedGaussian_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Barrier') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Barrier = dto.Barrier_fromJSON_string(jstr1);
        const obj2: Barrier = dto.Barrier_fromJSON_string(jstr2);
        if(!dto.Barrier_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'HistogramAxis') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: HistogramAxis = dto.HistogramAxis_fromJSON_string(jstr1);
        const obj2: HistogramAxis = dto.HistogramAxis_fromJSON_string(jstr2);
        if(!dto.HistogramAxis_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Histogram') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Histogram = dto.Histogram_fromJSON_string(jstr1);
        const obj2: Histogram = dto.Histogram_fromJSON_string(jstr2);
        if(!dto.Histogram_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'EvaluationPoint') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: EvaluationPoint = dto.EvaluationPoint_fromJSON_string(jstr1);
        const obj2: EvaluationPoint = dto.EvaluationPoint_fromJSON_string(jstr2);
        if(!dto.EvaluationPoint_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'EvaluationResults') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: EvaluationResults = dto.EvaluationResults_fromJSON_string(jstr1);
        const obj2: EvaluationResults = dto.EvaluationResults_fromJSON_string(jstr2);
        if(!dto.EvaluationResults_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Parameter') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Parameter = dto.Parameter_fromJSON_string(jstr1);
        const obj2: Parameter = dto.Parameter_fromJSON_string(jstr2);
        if(!dto.Parameter_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Model') {
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: Model = dto.Model_fromJSON_string(jstr1);
        const obj2: Model = dto.Model_fromJSON_string(jstr2);
        if(!dto.Model_equal(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);

    } else
        throw new Error(`Cannot compare an object of the structure ${struct_name}.`);
}

function main () {
    // expect at least 3 args
    if(process.argv.length<3)
        throw new Error(`Expect at least 3 args, found ${process.argv.length}`);

    var command = process.argv[2];

    if(command=='create'){
        if(process.argv.length<5)
            throw new Error(`Command "${command}" expects at least 5 args, found ${process.argv.length}`);
        create(process.argv[3],process.argv[4]);
    }
    else if(command=='convert'){
        if(process.argv.length<6)
            throw new Error(`Command "${command}" expects at least 6 args, found ${process.argv.length}`);
        convert(process.argv[3],process.argv[4],process.argv[5]);
    }
    else if(command=='compare'){
        if(process.argv.length<6)
            throw new Error(`Command "${command}" expects at least 6 args, found ${process.argv.length}`);
        compare(process.argv[3],process.argv[4],process.argv[5]);
    } else
        throw new Error(`Unknown command "${command}"`);
}

main();

