function login() {
	alert("로그인 상세 페이지로 전환.");
}

function makereview() {
	alert("리뷰하기 페이지로 전환.");
}

function bookopne() {
	alert("해당 책 상세 페이지로 전환.");
}

function setTopBannerBookList(bookListData) {
	let bookList = bookListData.sort(function (a, b) {
		if (a.hasOwnProperty("likeCount")) {
			return b.likeCount - a.likeCount;
		}
	});

	let firstBook = bookList[0];

	let summary = firstBook["bookSummary"].substring(0, 20) + "...";

	let temp_next_html = `<button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active"
            aria-current="true" aria-label="Slide 1"></button>`;

	let temp_html = `
						<div class="carousel-item active" data-bs-interval="1000">
						<button onclick="bookopne()">
							<div class = "cardimage">
							<img src="${firstBook["bookThumbnail"]}" class="d-block w-100" alt="...">
							</div>
							<div class="carousel-caption d-none d-md-block">
								<div class= "cardtext" >
								<h5>${firstBook["bookTitle"]}</h5>
								<p>${summary}</p>
								</div>
							</div>
						</button>
						</div>`;

	$("#topCardIndexButton").append(temp_next_html);
	$("#topCardItem").append(temp_html);

	for (let i = 1; i < 4; i++) {
		let book = bookList[i];

		let summary = book["bookSummary"].substring(0, 20) + "...";

		let temp_next_html = `<button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="${i}"
                aria-label="Slide ${i + 1}"></button>`;

		let temp_html = `
							<div class="carousel-item" data-bs-interval="2000">
								<button onclick="bookopne()">
									<div class = "cardimage">
										<img src="${book["bookThumbnail"]}" class="d-block w-100" alt="...">
									</div>
									<div class="carousel-caption d-none d-md-block">
										<div class= "cardtext" >
											<h5>${book["bookTitle"]}</h5>
											<p>${summary}</p>
										</div>
									</div>
								</button>
							</div>
						`;

		$("#topCardIndexButton").append(temp_next_html);
		$("#topCardItem").append(temp_html);
	}
}

function setBookList(bookListData) {
	let bookList = bookListData;

	for (let i = 0; i < bookList.length; i++) {
		let book = bookList[i];

		let temp_html = `<div class="col">
											<div class="card h-10" style="width: 200px">
													<button onclick="bookopne()">
															<img src="${book["bookThumbnail"]}"
																	class="card-img-top">
															<div class="card-body">
																	<h5 class="card-title">${book["bookTitle"]}</h5>
																	<div style="text-align: right" ;>
																			<p class="card-text">
																					좋아요 : ${book["likeCount"]}</p>
																	</div>
															</div>
													</button>
											</div>`;

		$("#cards-box").append(temp_html);
	}
}

function getBookList() {
	$.ajax({
		type: "GET",
		url: "/api/book/list",
		data: {},
		success: function (response) {
			setTopBannerBookList(response["bookList"]);
			setBookList(response["bookList"]);
		},
	});
}
