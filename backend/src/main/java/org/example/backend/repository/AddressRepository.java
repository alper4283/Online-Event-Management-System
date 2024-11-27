package org.example.backend.repository;

import org.example.backend.entity.Address;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface AddressRepository extends BaseRepository<Address, Long> {

    @Query(value = "SELECT * FROM address LIMIT 10", nativeQuery = true)
    List<Address> findTop10();
}
