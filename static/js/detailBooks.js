function addLike() {
	const receivedData = location.href.split("?")[1];
	$.ajax({
		type: "POST",
		url: "/api/book/like/plus",
		data: { bookId: receivedData },
		success: function (response) {
			if (response.result == "success") {
				alert("추천 성공");
			} else {
				alert("추천 실패");
			}
		},
	});
}
function addDislike() {
	const receivedData = location.href.split("?")[1];
	$.ajax({
		type: "POST",
		url: "/api/book/dislike/plus",
		data: { bookId: receivedData },
		success: function (response) {
			if (response.result == "success") {
				alert("비추 성공");
			} else {
				alert("비추 실패");
			}
		},
	});
}

function addComment() {
	const receivedData = location.href.split("?")[1];

	let comment = $("#replyInput").val();

	$.ajax({
		type: "POST",
		url: "/api/comment",
		data: { bookId: receivedData, comment: comment },
		success: function (response) {
			window.location.reload();
		},
	});
}

function getBookDetail() {
	const receivedData = location.href.split("?")[1];
	$.ajax({
		type: "GET",
		url: "/api/book/detail",
		data: { bookId: receivedData },
		success: function (response) {
			let book = response.book;
			let commentList = book.comment;
			$("#bookTitle").text(book.bookTitle);
			$("#bookAuthor").text(book.bookAuthor);
			$("#bookPublisher").text(book.bookPublisher);
			$("#bookSummary").text(book.bookSummary);
			// $("#likeCount").text(book.likeCount);
			// $("#disLikeCount").text(book.disLikeCount);
			$("#bookThumbnail").attr("src", book.bookThumbnail);

			for (let i = 0; i < commentList.length; i++) {
				let comment = commentList[i];

				let temp_html = `<li class="list-group-item">${comment.comment}</li>`;

				$("#replyUl").append(temp_html);
			}
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
			} else {
				$("#loginBtn").css("display", "Bolck");
				$("#signUpBtn").css("display", "Bolck");
			}
		},
	});
}
