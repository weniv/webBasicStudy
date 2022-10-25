fetch("http://test.api.weniv.co.kr/mall")
    .then((data) => data.json())
    .then((data) => console.log(data));

fetch("http://test.api.weniv.co.kr/mall")
    .then(function (response) {
        return response.json();
    })
    .then((json) => {
        json.forEach((item) => {
            const imgElement = document.createElement("img");
            const h1Element = document.createElement("h1");

            const imgURL =
                "http://test.api.weniv.co.kr/" + item["thumbnailImg"];
            imgElement.src = imgURL;
            h1Element.innerText = item["productName"];

            document.body.append(h1Element);
            document.body.append(imgElement);
        });
    });
