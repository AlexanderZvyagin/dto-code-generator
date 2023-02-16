
// This file was automatically generated!
// - by <software> <version>
// - from <DTO-s spec>

import * as fs from 'fs'
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

function random_float(min:number = -1e6, max:number = 1e6) : number {
    return random_int();
}

function random_string(min:number = 0, max:number = 3) : string {
    let out: string = '';
    const input: string = 'abcdefghijklmnopqrstuvwxyz0123456789';
    for (let i = 0; i < 32; i++)
        out += input.charAt(random_int(0,input.length));
    return out;
}

function random_list_of_ints (min:number = 0, max:number = 3) : number[] {
    const size = random_int(min,max);
    let list:number[] = [];
    for(let i=0; i<size; i++)
        list.push(random_int());
    return list;
}

function random_list_of_floats (min:number = 0, max:number = 3) : number[] {
    const size = random_int(min,max);
    let list:number[] = [];
    for(let i=0; i<size; i++)
        list.push(random_float());
    return list;
}

function random_list_of_strings (min:number = 0, max:number = 3) : string[] {
    const size = random_int(min,max);
    let list:string[] = [];
    for(let i=0; i<size; i++)
        list.push(random_string());
    return list;
}


// https://stackoverflow.com/questions/1068834/object-comparison-in-javascript/6713782#6713782
function object_equals( x, y ) {
    if ( x === y ) return true;
      // if both x and y are null or undefined and exactly the same
  
    if ( ! ( x instanceof Object ) || ! ( y instanceof Object ) ) return false;
      // if they are not strictly equal, they both need to be Objects
  
    if ( x.constructor !== y.constructor ) return false;
      // they must have the exact same prototype chain, the closest we can do is
      // test there constructor.
  
    for ( var p in x ) {
      if ( ! x.hasOwnProperty( p ) ) continue;
        // other properties were tested using x.constructor === y.constructor
  
      if ( ! y.hasOwnProperty( p ) ) return false;
        // allows to compare x[ p ] and y[ p ] when set to undefined
  
      if ( x[ p ] === y[ p ] ) continue;
        // if they have the same strict value or identity then they are equal
  
      if ( typeof( x[ p ] ) !== "object" ) return false;
        // Numbers, Strings, Functions, Booleans must be strictly equal
  
      if ( ! object_equals( x[ p ],  y[ p ] ) ) return false;
        // Objects and Arrays must be tested recursively
    }
  
    for ( p in y )
      if ( y.hasOwnProperty( p ) && ! x.hasOwnProperty( p ) )
        return false;
          // allows x[ p ] to be set to undefined
  
    return true;
}


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


function random_list_of_UpdaterDoc (min:number = 0, max:number = 3) : UpdaterDoc[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:UpdaterDoc[] = [];
    for(let i=0; i<size; i++)
        list.push(random_UpdaterDoc());
    return list;
}


function random_UpdaterDto () : UpdaterDto {
    return new UpdaterDto (
        random_string(),
        random_list_of_ints(),
        random_list_of_floats(),
        random_float()

    );
}


function random_list_of_UpdaterDto (min:number = 0, max:number = 3) : UpdaterDto[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:UpdaterDto[] = [];
    for(let i=0; i<size; i++)
        list.push(random_UpdaterDto());
    return list;
}


function random_Updater () : Updater {
    return new Updater (
        random_string(),
        random_list_of_ints(),
        random_list_of_floats(),
        random_float()

    );
}


function random_list_of_Updater (min:number = 0, max:number = 3) : Updater[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Updater[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Updater());
    return list;
}


function random_IndependentGaussian () : IndependentGaussian {
    return new IndependentGaussian (
        random_list_of_ints()

    );
}


function random_list_of_IndependentGaussian (min:number = 0, max:number = 3) : IndependentGaussian[] {
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


function random_list_of_CorrelatedGaussian (min:number = 0, max:number = 3) : CorrelatedGaussian[] {
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


function random_list_of_Barrier (min:number = 0, max:number = 3) : Barrier[] {
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


function random_list_of_HistogramAxis (min:number = 0, max:number = 3) : HistogramAxis[] {
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


function random_list_of_Histogram (min:number = 0, max:number = 3) : Histogram[] {
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


function random_list_of_EvaluationPoint (min:number = 0, max:number = 3) : EvaluationPoint[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:EvaluationPoint[] = [];
    for(let i=0; i<size; i++)
        list.push(random_EvaluationPoint());
    return list;
}


function random_EvaluationResults () : EvaluationResults {
    return new EvaluationResults (
        random_list_of_strings(),
        random_list_of_ints(),
        random_list_of_floats(),
        random_list_of_floats(),
        random_list_of_floats(),
        random_list_of_floats(),
        random_list_of_ints(),
        random_list_of_Histogram()

    );
}


function random_list_of_EvaluationResults (min:number = 0, max:number = 3) : EvaluationResults[] {
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


function random_list_of_Parameter (min:number = 0, max:number = 3) : Parameter[] {
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
        random_list_of_Updater(),
        random_list_of_EvaluationPoint(),
        random_float(),
        random_int()

    );
}


function random_list_of_Model (min:number = 0, max:number = 3) : Model[] {
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:Model[] = [];
    for(let i=0; i<size; i++)
        list.push(random_Model());
    return list;
}


function create (struct_name:string, file_name:string){
    if(false){

    } else if (struct_name === 'UpdaterDoc') {
        fs.writeFileSync(
            file_name,
            JSON.stringify (random_UpdaterDoc()));


    } else if (struct_name === 'UpdaterDto') {
        fs.writeFileSync(
            file_name,
            JSON.stringify (random_UpdaterDto()));


    } else if (struct_name === 'Updater') {
        fs.writeFileSync(
            file_name,
            JSON.stringify (random_Updater()));


    } else if (struct_name === 'IndependentGaussian') {
        fs.writeFileSync(
            file_name,
            JSON.stringify (random_IndependentGaussian()));


    } else if (struct_name === 'CorrelatedGaussian') {
        fs.writeFileSync(
            file_name,
            JSON.stringify (random_CorrelatedGaussian()));


    } else if (struct_name === 'Barrier') {
        fs.writeFileSync(
            file_name,
            JSON.stringify (random_Barrier()));


    } else if (struct_name === 'HistogramAxis') {
        fs.writeFileSync(
            file_name,
            JSON.stringify (random_HistogramAxis()));


    } else if (struct_name === 'Histogram') {
        fs.writeFileSync(
            file_name,
            JSON.stringify (random_Histogram()));


    } else if (struct_name === 'EvaluationPoint') {
        fs.writeFileSync(
            file_name,
            JSON.stringify (random_EvaluationPoint()));


    } else if (struct_name === 'EvaluationResults') {
        fs.writeFileSync(
            file_name,
            JSON.stringify (random_EvaluationResults()));


    } else if (struct_name === 'Parameter') {
        fs.writeFileSync(
            file_name,
            JSON.stringify (random_Parameter()));


    } else if (struct_name === 'Model') {
        fs.writeFileSync(
            file_name,
            JSON.stringify (random_Model()));

    } else
        throw new Error(`Cannot create an object of the structure ${struct_name}.`);
}

function convert (struct_name:string, file1_name:string, file2_name:string){
    if(false){

    } else if (struct_name === 'UpdaterDoc') {
        const obj = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'UpdaterDto') {
        const obj = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Updater') {
        const obj = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'IndependentGaussian') {
        const obj = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'CorrelatedGaussian') {
        const obj = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Barrier') {
        const obj = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'HistogramAxis') {
        const obj = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Histogram') {
        const obj = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'EvaluationPoint') {
        const obj = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'EvaluationResults') {
        const obj = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Parameter') {
        const obj = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        fs.writeFileSync(file2_name, JSON.stringify(obj));


    } else if (struct_name === 'Model') {
        const obj = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        fs.writeFileSync(file2_name, JSON.stringify(obj));

    } else
        throw new Error(`Cannot convert an object of the structure ${struct_name}.`);
}

function compare (struct_name:string, file1_name:string, file2_name:string){
    if(false){

    } else if (struct_name === 'UpdaterDoc') {
        const obj1 = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        const obj2 = JSON.parse((fs.readFileSync(file2_name,'utf-8')));
        if(!object_equals(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'UpdaterDto') {
        const obj1 = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        const obj2 = JSON.parse((fs.readFileSync(file2_name,'utf-8')));
        if(!object_equals(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Updater') {
        const obj1 = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        const obj2 = JSON.parse((fs.readFileSync(file2_name,'utf-8')));
        if(!object_equals(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'IndependentGaussian') {
        const obj1 = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        const obj2 = JSON.parse((fs.readFileSync(file2_name,'utf-8')));
        if(!object_equals(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'CorrelatedGaussian') {
        const obj1 = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        const obj2 = JSON.parse((fs.readFileSync(file2_name,'utf-8')));
        if(!object_equals(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Barrier') {
        const obj1 = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        const obj2 = JSON.parse((fs.readFileSync(file2_name,'utf-8')));
        if(!object_equals(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'HistogramAxis') {
        const obj1 = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        const obj2 = JSON.parse((fs.readFileSync(file2_name,'utf-8')));
        if(!object_equals(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Histogram') {
        const obj1 = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        const obj2 = JSON.parse((fs.readFileSync(file2_name,'utf-8')));
        if(!object_equals(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'EvaluationPoint') {
        const obj1 = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        const obj2 = JSON.parse((fs.readFileSync(file2_name,'utf-8')));
        if(!object_equals(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'EvaluationResults') {
        const obj1 = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        const obj2 = JSON.parse((fs.readFileSync(file2_name,'utf-8')));
        if(!object_equals(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Parameter') {
        const obj1 = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        const obj2 = JSON.parse((fs.readFileSync(file2_name,'utf-8')));
        if(!object_equals(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);


    } else if (struct_name === 'Model') {
        const obj1 = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        const obj2 = JSON.parse((fs.readFileSync(file2_name,'utf-8')));
        if(!object_equals(obj1,obj2))
            throw new Error(`${struct_name} objects are not equal.`);

    } else
        throw new Error(`Cannot compare an object of the structure ${struct_name}.`);
}

function main () {
    console.log(`echo I am the typescript with ${process.argv.length} arguments`);
    console.log(process.argv);

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

