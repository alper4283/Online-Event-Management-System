package org.example.backend.repository;

import org.example.backend.entity.Category;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface CategoryRepository extends BaseRepository<Category, Long> {

    @Query(value = "SELECT * FROM categories  LIMIT 10", nativeQuery = true)
    List<Category> findTop10();

}
