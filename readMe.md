<h2 id='contents'>Contents</h2>

<ol>
    <li>
        <a href='#finance-calculator'>Finance Calculator - finance_calculators.py</a>
    </li>
    <li>
        <a href='#task-manager-v1'>Task Manager - task_manager_v1.py</a>
    </li>
    <li>
        <a href='#task-manager-v2'>Task Manager - task_manager_v2.py</a>
    </li>
    <li>
        <a href='#inventory'>Inventroy -inventory.py</a>
    </li>
    <li>
        <a href='#bookstore' disabled>Bootstore- tbc</a>
    </li>
    <li>
        <a href='#install'>Installation Guide</a>
    </li>

</ol>

<h2 id='finance-calculator'>Finance Calculator</h2>
    <h3>File</h3>
        <a href='/finance_calculators.py'>finance_calculators.py</a>
    <h3>Description</h3>
        <p>
            The purpose of this task was to demonstrate an understanding of Variables and Control Structures.
        </p>
        <p>
        <p>
            The program offers the user 2 calculations to choose from: how much a monthly mortgage (or bond) repayment would be, and how much interest they may see as a return on an investment.
        </p>
        <p>
            The formula for these calculations is included in the file.
        <p>
            The program itself works using if statements that are built around the formula, and the information that a user needs to supply in order to run the calculation.
        </p>
        <p>
            This program was created based on a task that is early on in the course.
        </p>
    <h6>[<a href='#contents'>To Contents</a>]</h6>

<h2 id='task-manager'>Task Manager V1</h2>
    <h3>File</h3>
        <a href='/task_manager_v1.py'>task_manager.py</a><br>
        <a href='/tasks_v1.txt'>tasks_v1.txt</a><br>
        <a href='/user_v1.txt'>user_v1.txt</a><br>
    <h3>Description</h3>
        <p>
            The purpose of this program is to demonstrate an understanding of working with external data sources using the read/write functionality within Python.
        </p>
        <p>
            The program provides the user with a task management interface that allows for information to be read from, and written to, tasks.txt by selecting options from an interactive  menu.
        </p>
        <p>
            The program requires the user to login prior to being able to access any of the functionality, with the usernames and passwords stored in user.txt.
        </p>
        <p>
            Some functionality, such as registering new users, is limited to the admin only. An additional check is also included within the program to prevent tasks being assinged to names that are not registered in the users.txt file.
        </p>
    <h3>Useage</h3>
    <p>
        The following format must be maintained within the <b>user.txt</b> file in order for the program to run:
        <ul>
            <li>Only one username and password per line</li>
            <li>Each line must record username then password, sepearted by ", ". EG: usename, password</li>
        </ul>
    </p>
    <p>
        The following format must be maintained within the <b>tasks.txt</b> file in order for the program to run:
        <ul>
            <li>Only one task per line</li>
            <li>Each data point must be seperated by ", " EG data1, data2, data3</li>
            <li>The sequence of data must follow this format:
                <ol>
                    <li>username</li>
                    <li>task name</li>
                    <li>task decription</li>
                    <li>date added as DD Mon YYYY</li>
                    <li>task due date as DD Mon YYYY</li>
                    <li>completion status as Yes/No</li>
                </ol>    
            </li>
        </ul>
    </p>
    <h6>[<a href='#contents'>To Contents</a>]</h6>

<h2 id='task-manager-v2'>Task Manager V2</h2>
    <h3>File</h3>
        <a href='/task_manager_v2.py'>task_manager_v2.py</a><br>
        <a href='/tasks_v2.txt'>tasks_v2.txt</a><br>
        <a href='/user_v2.txt'>user_v2.txt</a><br>
        <a href='/task_overview.txt.'>task_overview.txt</a><br>
        <a href='/user_overview.txt'>user_overview.txt</a><br>
    <h3>Description</h3>
        <p>
            The purpose of this task was to demonstrate an understanding of Lists, Functions, and String Handling, building on the previous version of the Task Manager program to integrate functions and handle slightly more complex tasks using the read/write functionality of Python.
        </p>
        <p>
            The program builds on the same functionality offered by Task Manager V1, replacing if/else logic in the main body of the code with functions where possible.
        </p>
        <p>
            In addition to the useof functions, this version of the Task Manager program also introduces new text files that display statistics generated from a combination of the tasks.txt and user.txt files.
        </p>
        <p>
            The report output is stored in <b>user_overview.txt</b> and <b>task_overview.txt</b>.
        </p>
    <h3>Useage</h3>
    <p>
        The following format must be maintained within the <b>user.txt</b> file in order for the program to run:
        <ul>
            <li>Only one username and password per line</li>
            <li>Each line must record username then password, sepearted by ", ". EG: usename, password</li>
        </ul>
    </p>
    <p>
        The following format must be maintained within the <b>tasks.txt</b> file in order for the program to run:
        <ul>
            <li>Only one task per line</li>
            <li>Each data point must be seperated by ", " EG data1, data2, data3</li>
            <li>The sequence of data must follow this format:
                <ol>
                    <li>username</li>
                    <li>task name</li>
                    <li>task decription</li>
                    <li>date added as DD Mon YYYY</li>
                    <li>task due date as DD Mon YYYY</li>
                    <li>completion status as Yes/No</li>
                </ol>    
            </li>
        </ul>
    </p>
    <h6>[<a href='#contents'>To Contents</a>]</h6>

<h2 id='Inventory'>Inventory</h2>
    <h3>File</h3>
        <a href='/inventory.py'>inventory.py</a><br>
        <a href='/intentoy.txt'>inventory.txt</a>
    <h3>Description</h3>
    <p>
        The purpose of this task was to demonstrate an uderstanding of Object-Oriented Programming with a program that emulates a stock management system for retailers selling shoes.
    </p>
    <p>
        The program reads data from the inventory stored in the inventory.txt file and creates objects for each stock item to capture the following information:
        <ul>
            <li>Country</li>
            <li>Product Code</li>
            <li>Product Name</li>
            <li>Product Cost</li>
            <li>Quantity / Stock Level</li>
        </ul>
    </p>
    <p>
        Users are able to interact with the inventory.txt file through a simple interface that provides the following functionality:
        <ul>
            <li>Add a new stock line</li>
            <li>View all stock items</li>
            <li>Update stock information</li>
            <li>Search for stock using the product code</li>
            <li>Calculate the value of each stock line</li>
            <li>Find the stock line that is currently in the sale</li>
        </ul>
    </p>
    <h3>Useage</h3>
    <p>
        In order for the program to work the data in <b>inventory.txt</b> must be formated using the following:
        <ol>
            <li>The first line must contain the data headings</li>
            <li>Data headings must be in this order:</li>
                <ol>
                    <li>Country</li>
                    <li>Product Code</li>
                    <li>Product Name</li>
                    <li>Product Cost</li>
                    <li>Quantity / Stock Level</li>
                </ol>
            <li>Data values must be seperated by a "," value. EG country,code, ...</li>
            <li>Cost must be an integer value</li>
            <li>Quantity must be an integer value</li>
        </ul>
    </p>
    <h6>[<a href='#contents'>To Contents</a>]</h6>

<h2 id='bookstore'>Bookstore</h2>
    <h3>File</h3>
        <p>TBC - in development</p>
    <h3>Description</h3>
        <p>
            TBC - in development
        </p>
    <h3>Useage</h3>
    <h6>[<a href='#contents'>To Contents</a>]</h6>

<h2 id='install'>Installation Guide</h2>
    <p>
        The following programs require specific versions of python and/or additional libraries to be installed in order to run:
        <ul>
            <li><a href='/task_manager_v2.py'>task_manager_v2.py</a></li>
                <ul>
                    <li><a href='https://www.python.org/downloads/release/python-3100/'>Python V3.10.0 as Match Case is used</a></li>
                </ul>
            <li><a href='/inventory.py'>inventory.py</a></li>
                <ul>
                    <li><a href='https://www.python.org/downloads/release/python-3100/'>Python V3.10.0 as Match Case is used</a></li>
                    <li><a href='https://pypi.org/project/tabulate/'>Tabulate library</a></li>
                </ul>
            <li>.txt files must be stored in the same directory as the program files</li>
        </ul>
    </p>
    <p>
        All programs have been written using Python Version 3.11.0 and it is recommends that they are run with this or a more recent version installed.
    </p>
    <h6>[<a href='#contents'>To Contents</a>]</h6>

