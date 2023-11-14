const pairedParentheses = (str) => {
    let count = 0;

    for (const char of str.split('')) {
        // console.log(char)
        if (char === `(`) {
            count++;
        } else if (char === `)`) {
            if (count < 1) return false;
            count--;
        }
    }

    return count === 0;
};

module.exports = {
    pairedParentheses,
};

console.log(pairedParentheses("))()"));