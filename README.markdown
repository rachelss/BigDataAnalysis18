## Website for BIO 181G at URI

## To use this as a template

1.  Read about [github pages](http://pages.github.com/).

2.  Log in to GitHub.
    (If you do not have an account, you can quickly create one for free.)
    You must be logged in for the remaining steps to work.

3.  Go to [GitHub's importer](http://import.github.com/new). *Do not fork this repository if you are creating your own course.*

4.  Paste the url of this repo as the old repository to clone:
    <https://github.com/SchwartzLabURI/Bio181G>.

5.  Select the owner for your new repository.
    (This will probably be you, but may instead be an organization you belong to.)

6.  Choose a name for your workshop website repository.

7.  Make sure the repository is public.

8.  Click "Begin Import".
    When the process is done,
    you will receive a message like
    "Importing complete! Your new repository myname/mycourse is ready."
    and you can go to the new repository by clicking on the name.

9.  Go into your newly-created repository,
    which will be at `https://github.com/myname/mycourse`.
    For example,
    if your username is `abc`,
    the repository's URL will be `https://github.com/abc/mycourse`.

10. Clone the repository to your local computer.
    
11.  Edit `_config.yml` to customize site-wide variables.
  - Update the URLs appropriately - `baseurl` will be the name of your repository & url should be the username.github.io/repositoryname.
    
12. Update `index.md` with the basic info about your course.

13. Create course contents in _posts/weeks and course info in _posts/info. 
  - File names need to start with a date and this date will determine the order. 
  - Posts must have a category ('contents' for weekly content and 'info' for general information).

14. Push to the gh-pages branch of your github reposity: `git push origin gh-pages`.

## License

This site was modified from http://p2pu.github.io/jekyll-course-template. The code is all released under the MIT license unless otherwise noted. By default the template is set up to publish the content you add under CC-BY-SA.
