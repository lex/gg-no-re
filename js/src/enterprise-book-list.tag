<enterprise-book-list>
    <table if = { this.books.length > 0 }>
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
                <td> { b.title } </td>
                <td> { b.author } </td>
                <td> { b.pages } </td>
                <td> { b.year } </td>
                <td> { b.publisher } </td>
            </tr>
        </tbody>
    </table>

    <style>
    <script>
        this.books = opts.books
    </script>
</enterprise-book-list>
