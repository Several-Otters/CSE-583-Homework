THIS IS PART 8!!!!

This was mostly done with stackoverflow and GeeksForGeeks articles. I tried to pivot out of using robots to do this and get myself really engaged, but I did need some robot help. Mostly it was me having an idea of what I wanted to do, and needing a few searches to find the code and options that let me do the thing.

I needed help importing and finding my working directory when not in a notebook. I also needed robot guidance on the use of the date time stuff.

ROBOT GENERATED ROBOT DISCLOSURE:
We debugged a Python FileNotFoundError that occurred when reading a CSV with a relative path. The issue was traced to the fact that Python resolves relative paths from the current working directory, not from the location of the script file. We discussed how launching the script from /home/david caused ../src/bicycle_data.csv to resolve to an unintended location.

We reviewed several approaches to locating the CSV file, including running the script from a different directory, using an absolute path, and the recommended solution of constructing the file path relative to the script using pathlib and __file__. We then walked through how Path(__file__).parent works, how the / operator joins path components, and why this approach is portable across different machines and operating systems.

We also discussed the possibility of changing Python's working directory programmatically with os.chdir(Path(__file__).parent). While this would allow relative file references to work as expected, we noted that changing the working directory introduces global side effects and is generally less robust than building paths explicitly from the script location.

Finally, we covered working with date-time data in Pandas. A column containing timestamps stored as strings in the format 10/02/2012 01:00:00 PM was converted to a true datetime type using pd.to_datetime(). Once converted, we examined how to extract components such as year, month, day, and hour using the .dt accessor, as well as how to verify that the conversion succeeded by checking that the column's dtype became datetime64[ns] instead of remaining an object string column.

