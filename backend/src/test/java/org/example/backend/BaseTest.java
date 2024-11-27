package org.example.backend;

import org.example.backend.repository.AddressRepository;
import org.example.backend.repository.AnnouncementRepository;
import org.example.backend.repository.CategoryRepository;
import org.example.backend.repository.EventCategoryRepository;
import org.example.backend.repository.EventRepository;
import org.example.backend.repository.EventServiceRepository;
import org.example.backend.repository.OrganizerRepository;
import org.example.backend.repository.RegistrationRepository;
import org.example.backend.repository.ReviewRepository;
import org.example.backend.repository.ServiceRepository;
import org.example.backend.repository.SpatialRefSysRepository;
import org.example.backend.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.test.context.junit.jupiter.SpringJUnitConfig;

@SpringBootTest
@SpringJUnitConfig
public abstract class BaseTest {

    @Autowired
    protected AddressRepository addressRepository;

    @Autowired
    protected AnnouncementRepository announcementRepository;

    @Autowired
    protected CategoryRepository categoryRepository;

    @Autowired
    protected EventCategoryRepository eventCategoryRepository;

    @Autowired
    protected EventRepository eventRepository;

    @Autowired
    protected EventServiceRepository eventServiceRepository;

    @Autowired
    protected OrganizerRepository organizerRepository;

    @Autowired
    protected RegistrationRepository registrationRepository;

    @Autowired
    protected ReviewRepository reviewRepository;

    @Autowired
    protected ServiceRepository serviceRepository;

    @Autowired
    protected UserRepository userRepository;

    @Autowired
    protected JdbcTemplate jdbcTemplate;

    @Autowired
    private SpatialRefSysRepository spatialRefSysRepository;

}
