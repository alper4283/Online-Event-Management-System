package org.example.backend.repository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Map;

@Repository
public class SpatialRefSysRepository {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    public List<Map<String, Object>> findTop10() {
        String sql = "SELECT * FROM spatial_ref_sys LIMIT 10";
        return jdbcTemplate.queryForList(sql);
    }
}

