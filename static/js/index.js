function modalShow() {
	let modalSide = document.querySelector(".modal-side");
	modalSide.classList.add("show");
}

function addbooklist() {
	let addbooklist = document.querySelector(".addbooklist");
	if (
		$("#booktitle").val().length >= 2 &&
		$("#author").val().length >= 2 &&
		$("#bookinfo").val().length >= 2 &&
		$("#publisher").val().length >= 2 &&
		$("#bookUrl").val().length >= 2
	) {
		// 데이터 전송 하기
		let doc = {
			bookTitleGive: $("#booktitle").val(),
			bookAuthorGive: $("#author").val(),
			bookThumbnailGive: $("#bookUrl").val(),
			bookPublisherGive: $("#publisher").val(),
			bookSummaryGive: $("#bookinfo").val(),
		};

		$.ajax({
			type: "POST",
			url: "/api/book/register",
			data: doc,
			success: function (response) {
				let modalSide = document.querySelector(".modal-side");
				modalSide.classList.remove("show");
			},
		});
	} else {
		alert("다시하셈");
	}
}

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

	for (let i = 0; i < 4; i++) {
		let book = bookList[i];

		let temp_html = `<div class="col p03">
											<div class="card h-100">
													<button class="testBton" style="padding: 3% 3% 0 3%;" onclick="location.href='detailBooks?${book["id"]}'">
															<div style="background-image: url(${book["bookThumbnail"]});
															background-size: 102%;
															background-position: 50% 50%;
															width: 100%;
															padding: 145% 0 0 0;
															border-radius: 16px 2px 2px 2px;"
																	class="card-img-top"></div>
															<div class="card-body">
																	<h5 class="card-title">${book["bookTitle"]}</h5>
																	<div style="text-align: right";>
																			<p class="card-text">
																					좋아요 : ${book["likeCount"]}</p>
																	</div>
															</div>
													</button>
											</div>`;

		$("#cards-box2").append(temp_html);
	}
}

function setBookList(bookListData) {
	let bookList = bookListData.sort(function (a, b) {
		if (a.hasOwnProperty("id")) {
			return b.id - a.id;
		}
	});

	for (let i = 0; i < bookList.length; i++) {
		let book = bookList[i];

		let temp_html = `<div class="col p03">
											<div class="card h-100">
													<button class="testBton" style="padding: 3% 3% 0 3%;" onclick="location.href='/detailBooks?${book["id"]}'">
															<div style="background-image: url(${book["bookThumbnail"]});
															background-size: 102%;
															background-position: 50% 50%;
															width: 100%;
															padding: 145% 0 0 0;
															border-radius: 16px 2px 2px 2px;"
																	class="card-img-top"></div>
															<div class="card-body">
																	<h5 class="card-title">${book["bookTitle"]}</h5>
																	<div style="text-align: right";>
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

function tokenCheck() {
	$.ajax({
		type: "GET",
		url: "/api/valid",
		data: {},
		success: function (response) {
			if (response.result == "success") {
				$("#loginBtn").css("display", "None");
				$("#signUpBtn").css("display", "None");
				$("#signOutBtn").css("display", "Bolck");
				$("#nickname").text(response.nickname);
			} else {
				$("#loginBtn").css("display", "Bolck");
				$("#signUpBtn").css("display", "Bolck");
				$("#signOutBtn").css("display", "None");
			}
		},
	});
}

function signOut() {
	document.cookie = "mytoken=";
	alert("로그아웃 완료!!");
	location.reload();
}
