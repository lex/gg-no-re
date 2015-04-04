<enterprise-book-list>
    <table if={ this.books.length > 0 }>
        <thead>
            <tr>
                <th>Title</th>
                <th>Author</th>
                <th>Pages</th>
                <th>Year</th>
                <th>Publisher</th>
            </tr>
        </thead>

        <tbody>
            <tr each={ b in this.books }>
                <td> <div style='max-width: 442px; word-wrap: break-word'> { b.title } </div></td>
                <td> <div style='max-width: 442px; word-wrap: break-word'> { b.author } </div></td>
                <td> <div style='max-width: 442px; word-wrap: break-word'> { b.pages } </div></td>
                <td> <div style='max-width: 442px; word-wrap: break-word'> { b.year } </div></td>
                <td> <div style='max-width: 442px; word-wrap: break-word'> { b.publisher } </div></td>
                <td> <a href='edit_book/{ b.db_id }'>edit</a> </td>
                <td> <a href='delete_book/{ b.db_id }'>delete</a> </td>
            </tr>
        </tbody>
    </table>

    <script>
        this.books = opts.books;
        this.edit_callback = opts.edit_callback;
    </script>
</enterprise-book-list>
