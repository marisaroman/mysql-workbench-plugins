# mysql-workbench-plugins
## Query and Result Formatter for Jira
Formats your query/queries and result set(s) for nicer display in JIRA (wraps queries with "{code:sql}" tag and uses pipes to format result set headers and values.) 
### example
    {code:sql}
    SELECT id, username
    FROM User
    WHERE   enabled = 0
    LIMIT 2;
    
    ||id||username||
    |2|someDisabledUser|
    |5|someOtherDisabledUser|
    {code}

### Installation
1. Download query_result_jira_formatter.py
2. In MySQL Workbench, click the Scripting menu > Install Plugin/Module...
3. Find and choose query_result_jira_formatter.py and click Open
4. Restart MySQL Workbench
### Usage
1. Select the query you want to format in a query editor tab (alternatively, you don't need to select anything and the script will iterate all queries in the query editor you're viewing and will execute them and collect result sets)
2. Click Tools > Utilities > Execute to JIRA Query Format
3. In the pane beneath the result grid, select Text Output
4. Copy the part of the formatted results you need (e.g. you can copy only the query, only the results, or both - you can copy all queries/results or only some)
5. Paste into JIRA
### Known Issues
1. NULL isn't correctly handled. I followed the example provided by the MySQL Workbench team to handle NULL values, but I end up with a blank whether the value was NULL or blank/empty. I need to file a bug with the MySQL Workbench team.
2. Sometimes, your query results include a completely empty row, and if your query results include that row, the row will be included in the JIRA format. I don't know what causes this empty row to be included in a result set. If you do, let me know so I can tweak the formatting script. If you see the empty row and don't want to include it in your Jira content, just don't select that row when you copy the formatted results (it's always the last row).
