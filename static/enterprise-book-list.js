riot.tag('enterprise-book-list', '<table> <thead> <tr> <th>Title</th> <th>Author</th> <th>Pages</th> <th>Year</th> <th>Publisher</th> </tr> </thead> <tbody> <tr each="{ b in books }"> <td> { b.title } </td> <td> { b.author } </td> <td> { b.pages } </td> <td> { b.year } </td> <td> { b.publisher } </td> </tr> </tbody> </table>', function(opts) {
        this.books = opts.books;
    
});
