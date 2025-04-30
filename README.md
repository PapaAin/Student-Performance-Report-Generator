# Student-Performance-Report-Generator

## Description
This Python project processes and evaluates student performance data from multiple sources to calculate final grades and generate summary reports. 
It reads student information, exercise completions, and exam scores from input files, computes total points and grades, and outputs the results in both human-readable and machine-readable formats.

## Key Features:

-	*__Grade Calculation Logic__*:
    -	Combines exercise and exam scores using a weighted method.
    -	Applies a grading scale to assign final grades based on total points.
      
- *__Flexible Data Input__*:
    - Supports structured input files containing:
        - Student IDs and names
        - Completed exercise counts
        - Exam scores
        - Course metadata (e.g., title and credits)
          
-	*__Automated Report Generation__*:
    -	Text Report: Formatted for readability, showing detailed per-student performance.
    -	CSV Report: Structured for data analysis or integration into other systems.
    
-	*__Data Aggregation__*:
    -	Sums exercise activity and exam scores per student.
    -	Matches records using unique student identifiers.
