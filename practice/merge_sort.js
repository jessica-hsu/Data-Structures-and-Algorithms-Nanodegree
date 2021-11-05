function merge(left, right) {
    merged = []
    left_index = 0
    right_index = 0

    while (left_index < left.length && right_index < right.length) {
        left_num = left[left_index];
        right_num = right[right_index];
        if (left_num >= right_num) { // if left number is bigger, put in new array
            merged.push(left_num);
            left_index += 1;
        } else { // right number is bigger. put in new array
            merged.push(right_num);
            right_index += 1;
        } 
    }
        
    
    //left array finished first and right array has leftovers. Append rest of right array
    if (left_index == left.length && right_index < right.length) {
        merged.concat(right.slice(right_index))
    } else if (right_index == right.length && left_index < left.length) { //right array finished first and left array has leftovers. Append rest of left array
        merged.concat(left.slice(left_index))
    } 
        
    return merged
}

function mergeSort(input) {
    if (input.length <= 1) {
        return input;
    }
    // split array into two pieces
    middle = parseInt(input.length / 2);
    left = input.slice(0, middle);
    right = input.slice(middle);

    // recursive calls to further split left and right sides in half
    left = mergeSort(left);
    right = mergeSort(right);

    // combine sorted left and right sides
    combined = merge(left, right);
    return combined;
}

array = [4, 6, 2, 5, 9, 8];
new_array = mergeSort(array)
console.log(new_array);