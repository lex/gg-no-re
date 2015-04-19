<reference-manager>
    <div class='row' if={ books.length > 0 }>
        <div class='small-12 small-centered columns'>
            <p align='center'>
                <enterprise-book-list books={ books }>
            </p>
        </div>
    </div>
    <div class='row'>
        <div class='small-12 small-centered columns'>
            <p align='center'><a href='add_book' class='button'>Add a new book</a></p>
        </div>
    </div>

    <div class='row' if={ articles.length > 0 }>
        <div class='small-12 small-centered columns'>
            <p align='center'>
                <enterprise-article-list articles={articles}>
            </p>
        </div>
    </div>
    <div class='row'>
        <div class='small-12 small-centered columns'>
            <p align='center'><a href='add_article' class='button'>Add a new article</a></p>
        </div>
    </div>

    <div class='row' if={ inproceedings.length > 0 }>
        <div class='small-12 small-centered columns'>
            <p align='center'>
                <enterprise-inproceedings-list inproceedings={inproceedings}>
            </p>
        </div>
    </div>
    <div class='row'>
        <div class='small-12 small-centered columns'>
            <p align='center'><a href='add_inproceedings' class='button'>Add an inproceedings</a></p>
        </div>
    </div>
    
    <script>
        this.content = opts.content
        this.books = this.content.books
        this.articles = this.content.articles
        this.inproceedings = this.content.inproceedings
    </script>
</reference-manager>

<enterprise-book-list>
    <table>
        <thead>
            <tr>
                <th each={ th in book_tableheads }>{ th }</th>
            </tr>
        </thead>
        <tbody>
            <tr each={ b in books }>
                <td style='max-width: 250px; word-wrap: break-word'> { b.author } </td>
                <td style='max-width: 250px; word-wrap: break-word'> { b.title } </td>
                <td style='max-width: 250px; word-wrap: break-word'> { b.pages } </td>
                <td style='max-width: 250px; word-wrap: break-word'> { b.year } </td>
                <td style='max-width: 250px; word-wrap: break-word'> { b.publisher } </td>
                <td> <a href='edit_book/{ b.db_id }'>edit</a> </td>
                <td> <a href='delete_book/{ b.db_id }'>delete</a> </td>
            </tr>
        </tbody>
    </table>

    <script>
        console.log(this.books)
        this.books = opts.books;
        console.log(this.books)
        console.log(this.books.length)
        this.book_tableheads = ['Title', 'Author', 'Pages', 'Year', 'Publisher'];
    </script>
</enterprise-book-list>

<enterprise-article-list>
    <table>
        <thead>
            <tr>
                <th each={ th in article_tableheads }>{ th }</th>
            </tr>
        </thead>
        <tbody>
            <tr each={ a in articles }>
                <td style='max-width: 250px; word-wrap: break-word'> { a.author } </td>
                <td style='max-width: 250px; word-wrap: break-word'> { a.title } </td>
                <td style='max-width: 250px; word-wrap: break-word'> { a.journal } </td>
                <td style='max-width: 250px; word-wrap: break-word'> { b.year } </td>
                <td style='max-width: 250px; word-wrap: break-word'> { b.volume } </td>
                <td> <a href='edit_article/{ a.db_id }'>edit</a> </td>
                <td> <a href='delete_article/{ a.db_id }'>delete</a> </td>
            </tr>
        </tbody>
    </table>

    <script>
        this.articles = opts.articles;
        this.article_tableheads = ['Author', 'Title', 'Journal', 'Year', 'Volume'];
    </script>
</enterprise-article-list>

<enterprise-inproceedings-list>
    <table>
        <thead>
            <tr>
                <th each={ th in inproceedings_tableheads }>{ th }</th>
            </tr>
        </thead>
        <tbody>
            <tr each={ i in inproceedings }>
                <td style='max-width: 250px; word-wrap: break-word'> { i.author } </td>
                <td style='max-width: 250px; word-wrap: break-word'> { i.title } </td>
                <td style='max-width: 250px; word-wrap: break-word'> { i.school } </td>
                <td style='max-width: 250px; word-wrap: break-word'> { i.year } </td>
                <td> <a href='edit_inproceedings/{ i.db_id }'>edit</a> </td>
                <td> <a href='delete_inproceedings/{ i.db_id }'>delete</a> </td>
            </tr>
        </tbody>
    </table>

    <script>
        this.inproceedings = opts.inproceedings;
        this.inproceedings_tableheads = ['Author', 'Title', 'School', 'Year'];
    </script>
</enterprise-inproceedings-list>
