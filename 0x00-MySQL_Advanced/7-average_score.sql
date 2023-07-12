-- Create stored procedure ComputeAverageScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_corrections INT;
    DECLARE avg_score FLOAT;

    -- Calculate total score and total number of corrections for the user
    SELECT SUM(score), COUNT(*) INTO total_score, total_corrections
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate average score
    IF total_corrections IS NULL OR total_corrections = 0 THEN
        SET avg_score = 0;
    ELSE
        SET avg_score = total_score / total_corrections;
    END IF;

    -- Update user's average score
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END //
DELIMITER ;

