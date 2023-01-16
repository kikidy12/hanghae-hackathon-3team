function saveReply() {
	let contents = $("#datgul_contents").val();
	contents;
	window.location.reload();
}
function addLike() {
	const receivedData = location.href.split("?")[1];
	$.ajax({
		type: "POST",
		url: "/api/book/like/plus",
		data: { bookId: receivedData },
		success: function (response) {
			window.location.reload();
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
			window.location.reload();
		},
	});
}

function addComment() {
	document.cookie =
		"mytoken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJoYXJyeSIsImV4cCI6MTY3MzkwMTAzOX0.FFk4o-FRdbFkaBvzc2lbpMbLGzPAVP4lrUcg23W_Soc";

	let comment = $("#replyInput").val();

	$.ajax({
		type: "POST",
		url: "/api/comment",
		data: { bookId: 1, comment: comment },
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
