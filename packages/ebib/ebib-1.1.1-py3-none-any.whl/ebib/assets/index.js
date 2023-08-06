import {EnglishStemmer} from './english-stemmer.js'

const data = await fetch('./data.json').then((res) => res.json())
const eng_stemmer = new EnglishStemmer()
const PAGE_SIZE = 20;
const THRESHOLD = 0.1;

let tags = [];
let active_tags = [];
let authors = [];
let active_authors = [];
let scores = [];
let selected_articles = [];
let page = 0;

const main_panel = document.getElementById('main-panel');
const authors_div = document.getElementById('authors');
const tags_div = document.getElementById('tags');
const query_input = document.getElementById('query');
const export_button = document.getElementById('export');

function update_view() {
	let actual_scores = scores;
	if (active_tags.length > 0) {
		actual_scores = actual_scores.filter(x => active_tags.every(y => data['pdfs'][x[0]]['tags'].includes(y)));
	}
	if (active_authors.length > 0) {
		actual_scores = actual_scores.filter(x => active_authors.every(y => data['pdfs'][x[0]]['authors'].includes(y)));
	}
	actual_scores = actual_scores.slice(page*PAGE_SIZE, (page+1)*PAGE_SIZE);

	main_panel.replaceChildren();

	for (let x of actual_scores) {
		const article = document.createElement('div');
		article.classList.add('article');
		const cbox = document.createElement('input');
		cbox.type = 'checkbox';
		cbox.classList.add('cbox');
		cbox.onchange = () => {
			if (cbox.checked) {
				selected_articles.push(x[0]);
			} else {
				selected_articles.splice(selected_articles.indexOf(x[0]), 1);
			}
			export_button.innerHTML = `Export ${selected_articles.length} items`;
		};
		article.appendChild(cbox);
		const doi = document.createElement('a');
		doi.classList.add('doi');
		doi.href = data['pdfs'][x[0]]['url'];
		doi.innerHTML = data['pdfs'][x[0]]['doi'];
		article.appendChild(doi);
		const date = document.createElement('span');
		date.classList.add('date');
		date.innerHTML = `${data['pdfs'][x[0]]['year']}/${data['pdfs'][x[0]]['month']}`;
		article.appendChild(date);
		const title = document.createElement('a');
		title.classList.add('title');
		title.href = `pdf/${x[0]}.pdf`;
		title.innerHTML = data['pdfs'][x[0]]['title'];
		article.appendChild(title);
		const aauthors = document.createElement('span');
		aauthors.classList.add('authors');
		aauthors.innerHTML = data['pdfs'][x[0]]['authors'].join('; ');
		article.appendChild(aauthors);

		main_panel.appendChild(article);
		//mstring += `<div class="article"><input type="checkbox" class="cbox"/><a class="doi" href="${data['pdfs'][x[0]]['url']}">${data['pdfs'][x[0]]['doi']}</a><span class="date">${data['pdfs'][x[0]]['year']}/${data['pdfs'][x[0]]['month']}</span><a class="title" href="pdf/${x[0]}.pdf">${data['pdfs'][x[0]]['title']}</a><span class="authors">${data['pdfs'][x[0]]['authors'].join(', ')}</span></div>`;
	}
	//main_panel.innerHTML = mstring;

	authors_div.replaceChildren(authors_div.children[0]);
	for (const auth of authors) {
		const btn = document.createElement('button');
		btn.innerHTML = auth;
		if (active_authors.includes(auth)) {
			btn.classList.add('selected');
			btn.onclick = () => {
				active_authors.splice(active_authors.indexOf(auth), 1);
				update_view();
			};
		} else {
			btn.onclick = () => {
				active_authors.push(auth);
				update_view();
			};
		}
		authors_div.appendChild(btn);
	}
	tags_div.replaceChildren(tags_div.children[0]);
	for (const tag of tags) {
		const btn = document.createElement('button');
		btn.innerHTML = tag;
		if (active_tags.includes(tag)) {
			btn.classList.add('selected');
			btn.onclick = () => {
				active_tags.splice(active_tags.indexOf(tag), 1);
				update_view();
			};
		} else {
			btn.onclick = () => {
				active_tags.push(tag);
				update_view();
			};
		}
		tags_div.appendChild(btn);
	}
}

function search_query() {
	const query = query_input.value.split(' ').map(x => eng_stemmer.stemWord(x.toLowerCase()));
	scores = [];
	for (const pdf in data['pdfs']) {
		let s = 0;
		for (const term of query) {
			const k1 = 1.2;
			const b = 0.75;
			const f = term in data['pdfs'][pdf]['index'] ? data['pdfs'][pdf]['index'][term] : 0;
			const idf = term in data['idf'] ? data['idf'][term] : 0;
			s += idf * f * (k1 + 1)/(f + k1 * (1 - b + b*data['pdfs'][pdf]['length']/data['avgdl']));
		}
		scores.push([pdf, s]);
	}
	scores.sort((a, b) => a[1] < b[1]);
	scores = scores.filter(x => x[1] > THRESHOLD);

	page = 0;
	authors = [];
	active_authors = [];
	tags = [];
	active_tags = [];
	for (const pdf_score of scores) {
		for (const auth of data['pdfs'][pdf_score[0]]['authors']) {
			if (!authors.includes(auth)) {
				authors.push(auth);
			}
		}
	}
	for (const pdf_score of scores) {
		for (const tag of data['pdfs'][pdf_score[0]]['tags']) {
			if (!tags.includes(tag)) {
				tags.push(tag);
			}
		}
	}

	update_view();
}

function value_or_none(a) {
	return a ? a : '';
}

function export_selected() {
	const article_array = [];
	for (let x of selected_articles) {
		article_array.push(`
@${data['pdfs'][x]['type']}{${x},
publisher = {${value_or_none(data['pdfs'][x]['publisher'])}},
number = {${value_or_none(data['pdfs'][x]['number'])}},
journal = {${value_or_none(data['pdfs'][x]['journal'])}},
doi = {${value_or_none(data['pdfs'][x]['doi'])}},
url = {${value_or_none(data['pdfs'][x]['url'])}},
pages = {${value_or_none(data['pdfs'][x]['pages'])}},
title = {${value_or_none(data['pdfs'][x]['title'])}},
volume = {${value_or_none(data['pdfs'][x]['volume'])}},
authors = {${value_or_none(data['pdfs'][x]['authors'].join(' and '))}},
issn = {${value_or_none(data['pdfs'][x]['issn'])}},
year = {${value_or_none(data['pdfs'][x]['year'])}},
month = {${value_or_none(data['pdfs'][x]['month'])}}
}
		`);
	}
	const a = document.createElement('a');
	const url = window.URL.createObjectURL(new Blob(article_array, {type: 'application/x-bibtex'}));
	a.href = url;
	a.download = 'citation.bib';
	a.click();
	setTimeout(() => window.URL.revokeObjectURL(url), 0);
}

update_view();
window.search_query = search_query;
window.export_selected = export_selected;
