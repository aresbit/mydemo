use std::io;
use std::io::prelude::*;
use std::fs::File;
use std::path::Path;

fn main() -> Result<(), io::Error> {

    let open_file = File::open(Path::new("src/main.rs"));
    let mut file = match open_file {
        Ok(file) => file,
        Err(e) => return Err(e),
    };

    let mut buffer = String::new();
    match file.read_to_string(&mut buffer) {
        Ok(_) => {},
        Err(e) => return Err(e),
    }

    println!("{buffer}");

    Ok(())

}
