function lowercaseCount(str) {
    const reg = /[a-z]/g;
    const result = str.match(reg);
    return result.length
}

console.log(lowercaseCount("abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"))