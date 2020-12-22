window.onload = function () {
    let result = {};
    let step = 0;
    function showQuestion(questionNumber) {
        document.querySelector('.question').innerHTML = quiz[step]['q'];
        let answer = '';
        for (let key in quiz[step]['a']) {
            answer += `<li data-v='${key}' class="answer-variant">${quiz[step]['a'][key]}</li>`;
        }
        document.querySelector('.answer').innerHTML = answer;
    }
    document.onclick = function (event) {
        event.stopPropagation();
        if (event.target.classList.contains('answer-variant') && step < quiz.length) {
            if (result[event.target.dataset.v] != undefined) {result[event.target.dataset.v]++;}
                else {result[event.target.dataset.v] = 0;} step++;
            if (step == quiz.length) {
                document.querySelector('.question').remove();
                document.querySelector('.answer').remove();
                showResult();
            }
            else {showQuestion();}
        }
        if (event.target.classList.contains('reload-button')) {
            location.reload();
        }
    }

    function showResult() {
        let key = Object.keys(result).reduce(function (a, b) { return result[a] > result[b] ? a : b });
        let answer = document.createElement('p');
        answer.classList.add('result');
        answer.innerHTML = answers[key]['description'];
        document.querySelector('main').appendChild(answer);

        let reloadButton = document.createElement('button');
        reloadButton.innerHTML = 'Пройти тест заново';
        reloadButton.classList.add('reload-button');
        document.querySelector('main').appendChild(reloadButton);
    }
    showQuestion();
}