function groupsReqListener() {
    const groupsList = document.getElementById('groups-list');

    const groups = JSON.parse(this.response);
    for (const group of groups) {
        let tr = document.createElement('tr');
        tr.classList.add('position-relative');
        let td = document.createElement('td');
        let a = document.createElement('a');
        a.innerText = group.fields.title;
        a.href = window.location.origin + '/cadet/' + group.pk;
        a.setAttribute('class', 'stretched-link text-decoration-none text-reset');
        td.append(a);
        tr.append(td);
        groupsList.append(tr);
    }
}

function subjectsReqListener() {
    const subjectsList = document.getElementById('subjects-list');

    const subjects = JSON.parse(this.response);
    for (const subject of subjects) {
        let tr = document.createElement('tr');
        tr.classList.add('position-relative');
        let td = document.createElement('td');
        let a = document.createElement('a');
        a.innerText = subject.fields.title;
        a.href = window.location.origin + '/cadet/subject/' + subject.pk;
        a.setAttribute('class', 'stretched-link text-decoration-none text-reset');
        td.append(a);
        tr.append(td);
        subjectsList.append(tr);
    }
}

function cadetsReqListener() {
    const cadets = JSON.parse(this.response.cadets);
    const groups = this.response.groups;
    const ranks = this.response.ranks;
    const template = this.response.template;
    const container = document.getElementById('content');
    let html = '';
    let rank, group, date;
    for (cadet of cadets) {
        cadet.rank = ranks.find(elem => elem.id == cadet.fields.rank);
        cadet.group = groups.find(elem => elem.id == cadet.fields.group);
        date = new Date(cadet.fields.birthdate);
        cadet.fields.birthdate = date.toLocaleDateString();
        html += renderTemplate(template.cadet, {cadet: cadet})
    }
    let content = renderTemplate(template.container, {content: html});
    container.innerHTML = content;
}

function renderTemplate(str, data) {
    return str.replace(/\$\{([^}]+)\}/g, (match, key) => {
        const value = key.trim().split('.').reduce((acc, prop) => acc?.[prop], data);
        return value !== undefined ? value : match;
    });
}

function sendRequest(path, listener) {
    const req = new XMLHttpRequest();
    req.responseType = 'json';
    req.addEventListener('load', listener);
    req.open('GET', window.location.origin + '/cadet/api/' + path);
    req.send();
}

document.addEventListener('DOMContentLoaded', () => {
    sendRequest('groups', groupsReqListener);
    sendRequest('subjects', subjectsReqListener);

    document.getElementById('breadcrumb-cadets').addEventListener('click', () => {
        sendRequest('cadets', cadetsReqListener);
    });
});


