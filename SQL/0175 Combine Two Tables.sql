-- LeetCode
-- Problem: Combine Two Tables
-- Difficulty: Easy
-- URL: https://leetcode.com/problems/combine-two-tables/

SELECT 
    p.firstName, 
    p.lastName, 
    a.city, 
    a.state
FROM 
    Person p
LEFT JOIN 
    Address a 
ON 
    a.personId = p.personId;
