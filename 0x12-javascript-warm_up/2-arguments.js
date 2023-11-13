const Numargs = process.argv.lenght - 2;

if (Numargs === 0){
    console.log("No argument");
}
    else if (Numargs === 1){
        console.log("Argument found");
    }
    else{
        console.log("Arguments found");
    }
