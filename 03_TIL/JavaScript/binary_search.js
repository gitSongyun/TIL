const arr = [1, 2, 3, 10, 56, 78, 82, 85, 90];
const target = 10;

function binarysearch(arr) {
  start = 0;
  mid = Math.floor(arr.length / 2);
  end = arr.length ;

  if (arr[mid] > target) {
    end = mid;
    return binarysearch(arr.slice(start, end));
  } else if (arr[mid] < target) {
    start = mid + 1;
    return binarysearch(arr.slice(start, end));
  } else if (arr[mid] === target) {
    return mid;
  }
  return false
}
const res = binarysearch(arr);
console.log(res);
