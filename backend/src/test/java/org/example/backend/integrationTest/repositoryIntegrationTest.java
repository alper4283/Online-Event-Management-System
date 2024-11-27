package org.example.backend.integrationTest;


import org.example.backend.entity.Address;
import org.example.backend.entity.Announcement;
import org.example.backend.entity.Category;
import org.example.backend.entity.Event;
import org.example.backend.entity.EventCategory;
import org.example.backend.entity.EventService;
import org.example.backend.entity.Organizer;
import org.example.backend.entity.Registration;
import org.example.backend.entity.Review;
import org.example.backend.entity.Service;
import org.example.backend.entity.User;
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
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;
import java.util.Map;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest
public class IntegrationTest {
    @Autowired
    private AddressRepository addressRepository;

    @Autowired
    private AnnouncementRepository announcementRepository;

    @Autowired
    private CategoryRepository categoryRepository;

    @Autowired
    private EventCategoryRepository eventCategoryRepository;

    @Autowired
    private EventRepository eventRepository;

    @Autowired
    private EventServiceRepository eventServiceRepository;

    @Autowired
    private OrganizerRepository organizerRepository;

    @Autowired
    private RegistrationRepository registrationRepository;

    @Autowired
    private ReviewRepository reviewRepository;

    @Autowired
    private ServiceRepository serviceRepository;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private SpatialRefSysRepository spatialRefSysRepository;
    @Test
    public void testFetch10RecordsFromAllTables() {
        List<Address> addresses = addressRepository.findTop10();
        assertThat(addresses.size()).isEqualTo(10);

        List<Announcement> announcements = announcementRepository.findTop10();
        assertThat(announcements.size()).isEqualTo(10);

        List<Category> categories = categoryRepository.findTop10();
        assertThat(categories.size()).isEqualTo(10);

        List<EventCategory> eventCategories = eventCategoryRepository.findTop10();
        assertThat(eventCategories.size()).isEqualTo(10);

        List<Event> events = eventRepository.findTop10();
        assertThat(events.size()).isEqualTo(10);

        List<EventService> eventServices = eventServiceRepository.findTop10();
        assertThat(eventServices.size()).isEqualTo(10);

        List<Organizer> organizers = organizerRepository.findTop10();
        assertThat(organizers.size()).isEqualTo(10);

        List<Registration> registrations = registrationRepository.findTop10();
        assertThat(registrations.size()).isEqualTo(10);

        List<Review> reviews = reviewRepository.findTop10();
        assertThat(reviews.size()).isEqualTo(10);

        List<Service> services = serviceRepository.findTop10();
        assertThat(services.size()).isEqualTo(10);

        List<User> users = userRepository.findTop10();
        assertThat(users.size()).isEqualTo(10);

        List<Map<String, Object>> spatialRefSys = spatialRefSysRepository.findTop10();
        assertThat(spatialRefSys.size()).isEqualTo(10);
    }
}