use std::io;

fn main(){
    println!("===== First Odd Even Program =====");
    let mut value = String::new();

    println!("Please Input Value :");
    io::stdin().read_line(&mut value).expect("Failed");
    let value:i32 = value.trim().parse().expect("Failed");

    odd_even(&value);
}

fn odd_even(value:&i32) {
    if value%2 == 0 {
        println!("The Value of {} is Even", value);
    }else {
        println!("The Value of {} is Odd", value);
    }
}
