pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
    let mut result = digits.clone();
    let mut carry = 1;
    for i in (0..digits.len()).rev() {
        let sum = digits[i] + carry;
        result[i] = sum % 10;
        carry = sum / 10;
    }
    if carry > 0 {
        result.insert(0, carry);
    }
    result
}