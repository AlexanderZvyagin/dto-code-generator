using System;

internal class Program
{
    static private void create (string struct_name, string file1) {
        Console.WriteLine("create: no code");
    }

    static private void convert (string struct_name, string file1, string file2) {
        Console.WriteLine("convert: no code");
    }

    static private void compare (string struct_name, string file1, string file2) {
        Console.WriteLine("compare: no code");
    }

    static void Main(string[] args) {
        var command = args[0];

        if(command=="create")
            create(args[1],args[2]);
        else 
        if(command=="convert")
            convert(args[1],args[2],args[3]);
        else
        if(command=="compare")
            compare(args[1],args[2],args[3]);
        else
            throw new ArgumentException($"Unknown command '{command}'");
    }
}
