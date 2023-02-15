import dto from './dto'

function create (struct_name:string, file_name:string){
    console.log(`create: ${struct_name} ${file_name}`);
    var v = dto[struct_name];
    if(!v)
        throw new Error(`Not found: ${struct_name}`);
}

function convert (struct_name:string, file1_name:string, file2_name:string){
    console.log(`convert: ${struct_name} ${file1_name} ${file2_name}`);
}

function compare (struct_name:string, file1_name:string, file2_name:string){
    console.log(`compare: ${struct_name} ${file1_name} ${file2_name}`);
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
