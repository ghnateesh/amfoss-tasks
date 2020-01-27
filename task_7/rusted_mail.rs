extern crate regex;
use regex::Regex;
use std::io;

fn main() {
    let mut arr = String::new();
    println!("Enter your email id :");
    let mut b1:String=io::stdin().read_line(&mut arr).unwrap().to_string();
    let n: Regex = Regex::new(r"^[A-Za-z0-9!#$%&'*+=?^_`{|}~.]+@[a-zA-z0-9]+\.[a-z]*").unwrap();
    let w=n.is_match( &mut arr);
    if w{
        println!("valid")
        }
    else{

        println!("invalid")
        }
}
